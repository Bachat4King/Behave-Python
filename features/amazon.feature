@web
Feature: Amazon Examples

  Background: Amazon: go to amazon website
    Given Go to https://www.amazon.com/

  Scenario Outline: search a product in amazon
    Given Enter <search_term> in search field and click search button
    When select the first product that has <product_name> in its name
    Then retrieve the price of the product

    Examples:
      | search_term   | product_name |
      | iphone        | 11           |
      | computer      | Dell         |
      | graphics card | RTX 3050     |


  Scenario: search and buy a product
    Given Enter RTX 3060 in search field and click search button
    When select the first product that has RTX in its name
    And add the product to the cart
    Then "Added to Cart" text is in the page
