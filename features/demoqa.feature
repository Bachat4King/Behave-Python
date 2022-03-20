@UI
Feature: demoqa.com tests

  Scenario: Interactions - Slider
    Given Go to https://demoqa.com/slider
    Then demoqa: slide the bar to "50" percent

  Scenario: Interactions - Sortable
    Given Go to https://demoqa.com/sortable
    Then demoqa: sort the list reversed
