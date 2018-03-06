# Great documentation at https://www.jetbrains.com/help/pycharm/bdd-testing-framework.html
# Created by saduk at 3/1/2018
Feature: Fizzbuzz
  # Enter feature description here
  In order to showcase my modulus and control flow skills
  As a developer
  I want to solve Fizzbuzz

  Scenario Outline: Fizzbuzz
    Given I have a number <input_num>
    When I call Fizzbuzz
    Then I should get back <output_exp>
    Examples:
      | input_num | output_exp |
      | 5         | 'Buzz'     |
      | 6         | 'Fizz'     |
      | 15        | 'Fizzbuzz' |
      | 14        | ''         |