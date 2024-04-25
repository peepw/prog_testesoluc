from behave import given, when, then

@given('eu tenho dois números inteiros: {num1:d} e {num2:d}')
def step_impl(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('eu calculo a média dos dois números inteiros')
def step_impl(context):
    context.media = (context.num1 + context.num2) / 2

@then('a média deve ser {media:f}')
def step_impl(context, media):
    assert context.media == media, f"Média incorreta. Esperada: {media}. Obtida: {context.media}"