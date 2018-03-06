from behave import *

use_step_matcher("re")


@given("I have a number (?P<input_num>.+)")
def step_impl(context, input_num):
    """
    :type context: behave.runner.Context
    :type input_num: str
    """
    raise NotImplementedError


@when("I call Fizzbuzz")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError


@then("I should get back (?P<output_exp>.+)")
def step_impl(context, output_exp):
    """
    :type context: behave.runner.Context
    :type output_exp: str
    """
    raise NotImplementedError
