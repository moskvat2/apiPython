from fastapi import FastAPI, HTTPException
import stripe, re
from datetime import datetime

stripe.api_key = "sk_test_51MSPccIYkGWVz4dSrxMEBf8JrqNDO1ku37HR5dpmQhsqNysUEPFBuxiSDexbrMjsTxnef3dyZbnObZSCLBPKKL1Y00zniQ3XAt"

# def sendCard():
#     # Criando um cartão de crédito
    
#     number_card = input("Informe o número do cartão com 16 digitos: ")
#     expire_month = input("Digite o mês de vencimento do cartão com 2 digitos: ")
#     expire_year = input("Digite o ano de vencimento do cartão com 4 digitos: ")
#     cvc_cod = input("Digite o código CVC: ")
    
#     try:
#         # if not isinstance(number_card, int):
#         #     print("Número do cartão inválido")
#         #     exit()

#         if not isinstance(expire_month, int):
#             print("Mês informado não é inteiro")
#             exit()
#         else:
#             if expire_month < 1 or expire_month > 12:
#                 print("Mês informado é inválido")
#                 exit()

#         if not isinstance(expire_year, int):
#             print("Número inválido")
#             exit()
#         else:
#             if expire_year < datetime.now().year:
#                 print("Ano informado do cartão é inválido")
#                 exit()
            
#         if not isinstance(cvc_cod, int):
#             print("Número inválido")
#             exit()
#         else:
#             if cvc_cod < 1 or cvc_cod > 999:
#                 print("Código CVC é inválido")
#                 exit()
            
#     except ValueError:
#         print("Número inválido")
#         exit()
    
#     token = stripe.Token.create(
#     card={
#         "number": number_card,
#         "exp_month": expire_month,
#         "exp_year": expire_year,
#         "cvc": cvc_cod
#     },
#     )
    
#     return token

# def sendPayment(amount_payment):
#     token = sendCard()
    
#     # Fazendo um pagamento
#     charge = stripe.Charge.create(
#     amount = amount_payment,  # Valor em centavos
#     currency="brl",
#     source=token.id,
#     description="Pagamento de exemplo"
#     )

#     print("Pagamento realizado com sucesso!")
#     print("ID da transação: ", charge.id)
    
#     return amount_payment
    
    
# def sendRefund(transaction_id):
#     # Fazendo o estorno
#     refund = stripe.Refund.create(
#     charge=transaction_id,
#     )

#     print("Estorno realizado com sucesso!")
#     print("ID do estorno: ", refund.id)


# def menu():
#     print("Selecione uma opção:")
#     print("1. Pagar")
#     print("2. Estorno")
#     print("3. Sair")
#     opcao = input()
#     return opcao


# opcao = menu()
# while opcao != "3":
#     if opcao == "1":
#         amount_payment = input("Informe o valor a ser pago: ")
#         sendPayment(amount_payment)
#     elif opcao == "2":
#         transaction_id = input("Informe o Id da Transação realizada: ")
#         sendRefund(transaction_id)
#     else:
#         print("Opção inválida. Tente novamente.")
#     opcao = menu()

###############################################################

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/payment/{order_id}")
async def send_payment(order_id: int, number_card: str, expire_month: int, expire_year: int, cvc_code: int):
    #validate card information
    if not is_valid_card(number_card, expire_month, expire_year, cvc_code):
        raise HTTPException(status_code=400, detail="Invalid card information")
    
    #process payment
    success = process_payment(number_card, expire_month, expire_year, cvc_code)
    if not success:
        raise HTTPException(status_code=500, detail="Payment processing failed")
    
    return {"status": "success", "order_id": order_id}

def is_valid_card(number_card: str, expire_month: int, expire_year: int, cvc_code: int) -> bool:
    number_card = number_card.replace(" ", "") # remove spaces
    number_card = number_card[::-1] # reverse the digits
    total = 0
    for i, digit in enumerate(number_card):
        digit = int(digit)
        if i % 2 == 0:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        total += digit
    if total % 10 == 0:
        return True
    else:
        return False

def process_payment(number_card: str, expire_month: int, expire_year: int, cvc_code: int) -> bool:
    #payment processing logic here
    return True


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=5000,
                log_level='info', reload=True)
