from tempoapiclient import client

tempo = client.Tempo(
    auth_token="7t34jjGvG35YTRJeXk9pVFhFTFgeAA",
    base_url="https://api.tempo.io/core/3")

worklogs = tempo.get_worklogs(
    dateFrom="2022-07-01",
    dateTo="2022-07-31"
    )

x = 0
for i in worklogs:
    x = x + 1
    print(x)
    print(i)
