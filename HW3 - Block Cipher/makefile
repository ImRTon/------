install:
	pip install -r requirements.txt
	mkdir test_enc
	mkdir test_dec

enc:
	python keyProducer.py
	python IVproducer.py
	python enc.py --mode ECB --output ./test_enc/ECB.png
	python enc.py --mode CTR --output ./test_enc/CTR.png
	python enc.py --mode Custom --output ./test_enc/Custom.png


dec:
	python dec.py -di ./test_enc/ECB.png -mode "ECB" -o ./test_dec/res_ECB.png
	python dec.py -di ./test_enc/CTR.png -mode "CTR" -o ./test_dec/res_CTR.png
	python dec.py -di ./test_enc/Custom.png -mode "Custom" -o ./test_dec/res_Custom.png




