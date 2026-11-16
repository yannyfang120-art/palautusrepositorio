*** Settings ***
Resource    resource.robot
Suite Setup    Open And Configure Browser
Suite Teardown    Close Browser
Test Setup    Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username    newuser
    Set Password    password123
    Set Password Confirmation    password123
    Click    button >> text=Register
    Get Text    body    *=    Welcome

Register With Too Short Username And Valid Password
    Set Username    ab
    Set Password    password123
    Set Password Confirmation    password123
    Click    button >> text=Register
    Get Text    body    *=    Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username    newuser
    Set Password    short
    Set Password Confirmation    short
    Click    button >> text=Register
    Get Text    body    *=    Password must be at least 8 characters long

Register With Username That Is Already In Use
    Create User    existinguser    password123
    Set Username    existinguser
    Set Password    password123
    Set Password Confirmation    password123
    Click    button >> text=Register
    Get Text    body    *=    Username is already in use

*** Keywords ***
Reset Application And Go To Register Page
    Reset Application
    Go To Register Page