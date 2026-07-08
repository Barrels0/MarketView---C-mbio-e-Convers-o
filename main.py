#streamlit run main.py
import streamlit as st
import requests 

if "historico" not in st.session_state: #cria uma memoria da atual sessão do usuario
    st.session_state["historico"] = [] #cria uma lista vazia na memoria

st.set_page_config(page_title="Dashboard", page_icon="money")

st.title("💸 Meu Dashboard Financeiro")

headers = {"User-Agent": "Mozilla/5.0"}
moedas = "USD-BRL,EUR-BRL,BTC-BRL"
url_api = f"https://economia.awesomeapi.com.br/json/last/{moedas}"

resposta = requests.get(url_api, headers=headers)

# 2. Verificação de segurança: Só prossegue se a resposta da API for sucesso (código 200)
if resposta.status_code == 200:
    dados = resposta.json()
    valor_dolar = dados["USDBRL"]["bid"]
    valor_euro = dados["EURBRL"]["bid"]
    valor_btc = dados["BTCBRL"]["bid"]
else:
    st.error(f"Erro ao conectar na API: {resposta.status_code}")
    st.stop() 
resposta = requests.get(url_api)

dados = resposta.json()
# "bid" é o valor de mercado
valor_dolar = dados["USDBRL"]["bid"]
valor_euro = dados["EURBRL"]["bid"]
valor_btc = dados["BTCBRL"]["bid"]

dolar_float = float(valor_dolar)#faz o string virar float
euro_float = float(valor_euro)
real_float = 1.0
btc_float = float(valor_btc)

var_dolar = dados ["USDBRL"]["pctChange"]
var_euro = dados ["EURBRL"]["pctChange"]
var_btc = dados ["BTCBRL"]["pctChange"]

st.subheader("Cotações em tempo real de moedas, ações e criptomoedas")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(label="Dólar Americano (USD)", value = f"R$ {dolar_float:.2f}", delta=f"{var_dolar}%")
with col2:
    st.metric(label="Euro (EUR)", value= f"R$ {euro_float:.2f}",delta=f"{var_euro}%") # o "%" serve para uma melhor formatação
with col3:
    st.metric(label="Bitcoin (BTC)", value= f"R$ {btc_float:.2f}",delta=f"{var_btc}%")
#st.metric é uma ferramenta nativa criada para gerar paines financeiros

st.divider()
with st.expander("📈 Tendência do Dólar (Últimos 7 dias)"):
    st.subheader("📈 Tendência do Dólar (Últimos 7 dias)")
    url_grafico = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/7" #pega a informação diretamente pelo link na API
    resposta_grafico = requests.get(url_grafico) #essa variavel vai armazenar o json do url_grafico
    dados_grafico = resposta_grafico.json() #transforma de string para json

    valores_dolar = []
    for dia in dados_grafico:
        valores_dolar.append(float(dia["bid"])) #extrair somente o bid do que esta dentro de dados_grafico

    valores_dolar.reverse() # A api entrega os valores de hoje até 7 dias atras mas nos queremos um grafico que mostre como esta 7 dias atras e como esta hoje

    st.line_chart(valores_dolar) #pega a lista de numeros e cria o grafico sozinho

with st.expander("📈 Tendência do Euro (Últimos 7 dias)"):
    st.subheader("📈 Tendência do Euro (Últimos 7 dias)")
    url_grafico = "https://economia.awesomeapi.com.br/json/daily/EUR-BRL/7" 
    resposta_grafico = requests.get(url_grafico) 
    dados_grafico = resposta_grafico.json() 

    valores_euro = []
    for dia in dados_grafico:
        valores_euro.append(float(dia["bid"])) 

    valores_euro.reverse()

    st.line_chart(valores_euro) 

with st.expander("📈 Tendência do Bitcoin (Últimos 7 dias)"):
    st.subheader("📈 Tendência do Bitcoin (Últimos 7 dias)")
    url_grafico = "https://economia.awesomeapi.com.br/json/daily/BTC-BRL/7" 
    resposta_grafico = requests.get(url_grafico)
    dados_grafico = resposta_grafico.json() 

    valores_btc = []
    for dia in dados_grafico:
        valores_btc.append(float(dia["bid"])) 

    valores_btc.reverse()

    st.line_chart(valores_btc)

st.divider()

st.subheader("Converter Moedas")

valor_digit = st.number_input("Digite o valor que deseja converter: ",min_value=0.0, format="%.2f")

origem,destino = st.columns(2)

with origem:
    moeda_origem = st.selectbox(
        "Moeda de origem:",
        ["Real (BRL)", "Dólar Americano (USD)", "Euro (EUR)", "Bitcoin (BTC)"]
    )

with destino:
    moeda_destino = st.selectbox(
        "Moeda de destino:",
        ["Dólar Americano (USD)", "Euro (EUR)", "Bitcoin (BTC)", "Real (BRL)"]
    )

taxas = {
    "Real (BRL)": real_float,
    "Dólar Americano (USD)": dolar_float,
    "Euro (EUR)": euro_float,
    "Bitcoin (BTC)": btc_float
}

if st.button("Calcular conversão"):
    taxa_origem = taxas[moeda_origem]
    taxa_destino = taxas[moeda_destino] #pega o valor que ficou inserido dentro de moeda_destino(string) e usa dentro da taxa e por isso a string dentro de taxas tem q ser igual as que estão no selectbox

    valor_reais = valor_digit * taxa_origem
    resultado = valor_reais / taxa_destino

    st.success(f"💰 Resultado: **{resultado:.5f}** (em {moeda_destino})")

    nova_conta = {
        "Valor Original": f"{valor_digit:.2f} {moeda_origem}",
        "Convertido para": f"{resultado:.2f} {moeda_destino}"
    }

    st.session_state["historico"].append(nova_conta)

st.divider()
st.subheader("📝 Histórico da Sessão")

if len(st.session_state["historico"]) > 0:
    st.dataframe(st.session_state["historico"], use_container_width=True)
else:
    st.info("Suas conversões aparecerão aqui!")

