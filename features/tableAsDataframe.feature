Feature: get table as dataframe

  Scenario: Wikipedia table as dataframe
    When get the table as a dataframe
    Then print the dataframe


    Scenario: get table
      Given Go to https://es.wikipedia.org/wiki/Anexo:Comunas_de_Santiago_de_Chile
      When get the table

