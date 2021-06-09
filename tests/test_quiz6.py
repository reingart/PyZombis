# Testing ex 1

def test_quiz6_1(page):
    # Go to http://localhost:8000/quiz/Quiz6.html
    page.goto("quiz/Quiz6.html")
    
    page.click("text=def dormir(dia_semana, dia_festivo):")
    page.press("text=def dormir(dia_semana, dia_festivo):", "ArrowDown")
    page.press("text=def dormir(dia_semana, dia_festivo):", "Tab")
    
    page.type("text=def dormir(dia_semana, dia_festivo):", "if not dia_semana or dia_festivo:")
    page.press("text=def dormir(dia_semana, dia_festivo):", "Enter")
    page.type("text=def dormir(dia_semana, dia_festivo):", "return True") 
    page.press("text=def dormir(dia_semana, dia_festivo):", "Enter")
    page.type("text=def dormir(dia_semana, dia_festivo):", "return False")

    # Run an check it passed all unit tests
    page.click("#q6_1 >> *css=button >> text=Run")

    page.hover("#q6_1 >> text=You passed:")
    assert page.inner_text("#q6_1 >> text=You passed:") == "You passed: 100.0% of the tests"