Feature: Tirar a media de dois números
    Scenario: Realizar uma soma e uma divisão
        Given eu tenho dois números inteiros: 10 e 4
        When eu somo os dois números inteiros e divido por 2
        Then o resultado deve ser 7

        Given eu tenho dois números inteiros: 3 e 9
        When eu somo os dois números inteiros e divido por 2
        Then o resultado deve ser 6