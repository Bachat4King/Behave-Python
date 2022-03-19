@api
Feature: API tests for https://reqres.in/api

  Background: Set Base Env
    Given API: set base url to "https://reqres.in/api"
    And API: set headers
      | Content-Type | application/json |

  Scenario: GET - LIST USERS
    Given API: send GET request to "/users?page=2"
    Then API: status code should be "200"

  Scenario:  POST - CREATE
    Given API: set payload
      | name     | job    |
      | morpheus | leader |
    When API: send POST request to "/users"
    Then API: status code should be "201"

  Scenario:  PUT - UPDATE
    Given API: set payload
      | name     | job           |
      | morpheus | zion resident |
    When API: send PUT request to "/users/2"
    Then API: status code should be "200"

  Scenario:  PATCH - UPDATE
    Given API: set payload
      | name     | job           |
      | morpheus | zion resident |
    When API: send PUT request to "/users/2"
    Then API: status code should be "200"

  Scenario:  DELETE - DELETE
    Given API: send DELETE request to "/users/2"
    Then API: status code should be "204"