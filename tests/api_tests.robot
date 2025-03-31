*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    OperatingSystem
Library    ../tests/resources/api_resources.py

Suite Setup    Load Test Data

*** Variables ***
${BASE_URL}    https://reqres.in/api

*** Test Cases ***
Get All Users
    [Tags]    GET
    ${response}=    GET    ${BASE_URL}/users
    Status Should Be    200    ${response}
    ${users}=    Set Variable    ${response.json()['data']}
    Length Should Be    ${users}    6

Create New User
    [Tags]    POST
    ${new_user}=    Create Dictionary    name=${TEST_DATA['name']}    job=Developer
    ${response}=    POST    ${BASE_URL}/users    json=${new_user}
    Status Should Be    201    ${response}
    Dictionary Should Contain Key    ${response.json()}    id

Update User
    [Tags]    PUT
    ${update_data}=    Create Dictionary    name=${TEST_DATA['name']}    job=Senior Developer
    ${response}=    PUT    ${BASE_URL}/users/2    json=${update_data}
    Status Should Be    200    ${response}
    Should Be Equal As Strings    ${response.json()['job']}    Senior Developer

*** Keywords ***
Load Test Data
    ${test_data}=    Get Test Data    users.json
    Set Suite Variable    ${TEST_DATA}    ${test_data}[0]