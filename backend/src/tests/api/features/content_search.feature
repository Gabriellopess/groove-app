Feature: Buscas por conteúdo
    
    Scenario: Buscar músicas por gênero existente 

    Given o SongService retorna as músicas “Lover”, “Vampire” e “August”
    When uma requisição "GET" for enviada para "/songs/songs_by_genre/Pop”
    Then o status da resposta deve ser "200"
    And o JSON da resposta deve conter uma lista de músicas do gênero “Pop” com os nomes “Lover”, “Vampire” e “August”.

    Scenario: Buscar músicas por ano de lançamento

    Given o SongService retorna as músicas “Lover” e “Cruel Summer”
    When uma requisição "GET" for enviada para "/songs/songs_by_year/2019”
    Then o status da resposta deve ser "200"
    And o JSON da resposta deve conter uma lista de músicas com o ano de lançamento “2019” com os nomes “Lover” e “Cruel Summer”

    Scenario: Buscar músicas por nome de música

    Given o SongService retorna as músicas “Lover” e “Cruel Summer”
    When uma requisição "GET" for enviada para "/songs/songs_by_artits/Taylor@Swift" 
    Then o status da resposta deve ser "200"
    And o JSON da resposta deve conter uma lista de músicas da “Taylor Swift” com os nomes “Lover” e “Cruel Summer”

    Scenario: Buscar por música inexistente

    Given o SongService não possui a música “Cedo ou tarde”
    When uma requisição "GET" for enviada para "/songs/get_by_artist/NX@Zero” 
    Then o status da resposta deve ser "404"
    And o JSON da resposta deve conter um campo "msg” com o valor "Sinto muito, “Cedo ou Tarde” não encontrada no sistema"

    Scenario: Buscar artista inexistente

    Given o SongService não possui a música “NX Zero”
    When uma requisição "GET" for enviada para "/search/” com o parâmetro de consulta “query” definido como "NX Zero”
    Then o status da resposta deve ser "404"
    And o JSON da resposta deve conter um campo "msg” com o valor 'Not Found'