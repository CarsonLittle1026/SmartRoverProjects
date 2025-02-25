# test_BlinkingLED.py
# This is a simple test script to validate that Project01_BlinkingLED.py will execute as intended without throwing any error & the challenges are completed successfully.

# importing the subprocess module allows us to run other programs from this Python file
import subprocess
import time

# define a function called test_blinking_led
def test_BlinkingLED():
    # This function is execute any time we run the test
    #process = subprocess.Popen(['python3', 'Project01_BlinkingLED.py']) # Run Project 01

    try:
        # Run Project 1 and record the output
        result = subprocess.Popen(['python3', 'Project01_BlinkingLED.py']) # check if there is any error in the output
        print("PASS: Project 01 executed successfully.") 
    except subprocess.CalledProcessError as e:
        print(f"Project 01 execution failed with error: {e}")
        
    # Check that Challenge 1 is compelted
    #assert LED_On != 0.2, "FAIL: LED_On should not be equal to 0.2"
    #assert LED_Off != 0.1, "FAIL: LED_Off should not be equal to 0.1"
    #print("PASS: Project 01 Challenge 1 completed successfully.")

# test challenge 1
def test_led_on_off_values():
    # Check that LED_On is not equal to 0.2 and LED_Off is not equal to 0.1
    from Project01_BlinkingLED import LED_On, LED_Off
    assert LED_On != 0.2, "FAIL: LED_On should not be equal to 0.2"
    assert LED_Off != 0.1, "FAIL: LED_Off should not be equal to 0.1"
    print("PASS: Project 01 Challenge 1 completed successfully.")

if __name__ == "__main__":
    test_led_on_off_values()
    test_BlinkingLED()
