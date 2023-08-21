import streamlit as st;


st.title("Calcular Valor de Material")
with st.form(key='include_cliente'):
    input_valorFolha = st.number_input(label='Valor da Folha')
    input_larguraFolha = st.number_input(label="Largura da Folha (mt): ")
    input_comprimentoFolha = st.number_input(label="Compr. da Folha (mt)")
    input_larPeca = st.number_input(label='Largura da peça(cm): ')
    input_compPeca = st.number_input(label='Comprimento da Peça(cm): ')
    input_button_submit = st.form_submit_button(label='Calcular')
    if input_button_submit:
        valorCHAPA = input_valorFolha
        valorFRETE = 0
        valorCORTE = 0
        valorCHAPA = valorFRETE + valorFRETE + valorCHAPA
        larguraCHAPA = input_larguraFolha
        comprimentoCHAPA = input_comprimentoFolha
        larguraCHAPA = input_larguraFolha
        comprimentoCHAPA = input_comprimentoFolha
        #descobrir area quadrada da chapa
        areaCHAPA = larguraCHAPA * comprimentoCHAPA
        #descobrir o valor do metro quadrado
        vMetroQuadrado = valorCHAPA / areaCHAPA        
        larguraCALCmm = input_larPeca
        comprimCALCmm = input_compPeca
        #converter medidas da peça em mt 
        larguraCALCmt = larguraCALCmm / 100
        comprimCALCmt = comprimCALCmm / 100
        #descobrir a area da peça calculada
        areaPEÇA = larguraCALCmt * comprimCALCmt
        #descobrir valor da peça
        valorDaPeca = areaPEÇA * vMetroQuadrado
        st.text(f' Total Bruto =    R$ {valorDaPeca}')        
        x = int(valorDaPeca + (0 if valorDaPeca % 1 ==  0 else 1))        
        st.text(f'Total Liquido =    R$ {float(x)}')
