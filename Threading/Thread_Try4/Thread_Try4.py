import logging
import threading
import time
from nrc_custom.Potentiostat import Technique

function1_flag = 0

def run_characterization(root_path, experiment_name, test, channel):
    test_name = f'{experiment_name}_{test}_Char'  # Ensure different than deposition test
    # Below is the directory for accessing USB0 biologic (aka biologic 1)
    #directory = 'C:/Github/LearnPython_Again/Threading/Thread_Try4/EC-Lab Development Package_Copy5/Examples/C-C++/VisualStudio/MFCStaticLink/output/'

    #directory = 'C:/Github/LearnPython_Again/Threading/Thread_Try4/EC-Lab Development Package_Copy5/Examples/C-C++/VisualStudio/MFCStaticLink/output/'

    directory = 'C:/EC-Lab Development Package_Latest/Examples/C-C++/VisualStudio/MFCStaticLink/output/'

    #directory = 'C:/Users/Blackr/Documents/EC-Lab Development Package_Copy5/Examples/C-C++/VisualStudio/MFCStaticLink/output_USB1/'
    experiment = Technique(root_path, test_name, directory, channel)

    # Step 1 - OCV for initial stabilization
    experiment.ocv(
        root_path,
        test_name,
        rest_time_T=30)

    # Step 2 - EIS for polarization resistance - just run a quick one at zero current
    experiment.geis(
        root_path,
        test_name,
        vs_initial='False',
        vs_final='False',
        initial_current_step=0,  # Zero current!
        final_current_step=0,
        amplitude=5E-6,
        frequency_number=10,  # Just a quick scan
        final_frequency=1,
        initial_frequency=200E3,
        duration_step=0,  # refers to how long to hold the voltage initially prior to any frequency measurement
        average_n_times=1)

    # Step 4 - Do multiple LSV
    experiment.cv(
        root_path,
        test_name,
        vs_initial=['True', 'False', 'False', 'True', 'False'],  # Start the run at OCV 'True'
        voltage_step=[0, 2, 1, 0, 1],  # [Ei,E1,E2,Ei,Ef] - essentially just go to 2.0 vs. Ag/AgCl and come back to 1 V
        scan_rate=[0.005] * 5,  # 5 mV
        record_every_dE=0.005)

    for i in range(9):  # Run 9 sweeps of 1 V --> 2 V --> 1 V
        experiment.cv(
            root_path,
            test_name,
            vs_initial=['False', 'False', 'False', 'False', 'False'],  # Start the run at OCV 'True'
            voltage_step=[1, 2, 1, 1, 1],
            # [Ei,E1,E2,Ei,Ef] - essentially just go to 2.0 vs. Ag/AgCl and come back to 1 V
            scan_rate=[0.005] * 5,  # 5 mV
            record_every_dE=0.005)

        # Step 3 - Run the Tafel characterization
    experiment.ca(
        root_path,
        test_name,
        vs_initial=['False'] * 9,
        voltage_step=[1.48, 1.42, 1.36, 1.30, 1.24, 1.18, 1.12, 1.06, 1.00],  # vs. Ag/AgCl
        duration_step=[300, 90, 90, 90, 90, 90, 90, 90, 90])

def thread_function1(name):
    logging.info("Thread %s: starting", name)
    function1_flag = 1
    run_characterization('C:/Github/LearnPython_Again/Threading/Thread_Try4/',"ex","one",0)
    time.sleep(5)
    function1_flag = 0
    logging.info("Thread %s: finishing", name)

def thread_function2(name):
    logging.info("Thread %s: starting", name)
    time.sleep(25)
    numb = 0
    while (function1_flag != 1):
        numb = numb + 1
        print("\nHey!" + str(numb))
        time.sleep(1)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function1, args=(1,))
    y = threading.Thread(target=thread_function2, args=(2,))
    logging.info("Main    : before running thread")
    x.start()
    y.start()

    logging.info("Main    : wait for the thread to finish")
    x.join()
    y.join()
    logging.info("Main    : all done")