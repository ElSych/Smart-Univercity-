import subprocess
import pyautogui
import pandas as pd

def sign_in(meetingid, name, pswd):
    subprocess.call("ZoomInstaller.exe")
    
    join_btn = pyautogui.locateCenterOnScreen('join_button.jpeg')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    meeting_id_btn =  pyautogui.locateCenterOnScreen('meeting_id_button.jpeg')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meetingid)

    name_button =  pyautogui.locateCenterOnScreen('name_button.jpeg')
    pyautogui.moveTo(name_button)
    pyautogui.click()
    pyautogui.write(name)

    join_btn = pyautogui.locateCenterOnScreen('join_btn.jpeg')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pswd.jpeg')
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press('enter')

#while True:

     #sign_in(m_id, , m_name, m_pswd)##