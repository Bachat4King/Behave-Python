@utils
Feature: utilities

  # Tables
  Scenario Outline: list of dictionaries
    Given visualize this list of dictionaries
      | label  | value         |
      | texto  | <search_term> |
      | number | <number>      |

    Examples:
      | search_term | number |
      | iphone      | number |

  Scenario Outline: Horizontal table
    Given visualize this horizontal table
      | search_term   | value   | anotherValue   |
      | <search_term> | <value> | <anotherValue> |

    Examples:
      | search_term | value       | anotherValue |
      | iphone      | 123123      | a            |
      | samsung     | 31212123123 | b            |
      | macbook     | 3121323     | c            |
      | kindle      | 123132      | d            |
      | kindle fire | 231132      | e            |

  Scenario: table of values (left column as key)
    Given Visualize this table
      | texto1 | valor1 |
      | texto2 | valor2 |
      | texto3 | valor3 |

    # Text
  Scenario: work with a context.text
    Given visualize the raw text
      """
      This is a raw text
      """

  # Context attributes
  Scenario: get context attributes
    Given visualize the scenario name
    And visualize the feature name
    And visualize the feature filename
    Then visualize the tags

    # Context variables

  Scenario: context variables
    Given print {{ context.name }} as a context variable