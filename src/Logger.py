def error(message: str):
    complete = f'\033[91m❌ ERROR: {message}\u001b[0m'
    print(complete)

def success(message: str):
    complete = f'\033[92m✅ SUCCESS: {message}\u001b[0m'
    print(complete)

def incame(message: str):
    complete = f'\033[92m⬇ {message}\u001b[0m'
    print(complete)

def spend(message: str):
    complete = f'\033[93m⬆ {message}\u001b[0m'
    print(complete)

def log(message = ''):
    print(f'\u001b[0m{message}\u001b[0m')

if __name__ == '__main__':
    success("Alguma mensagem")
    error("Alguma mensagem")
    spend('some spend')
    incame('some incame')
    log("some some")