render:
	./generate.py "CorePayment.xlsx" | pbcopy

pdf:
	rm -f cp.pdf
	./generate.py "CorePayment.xlsx" > cp.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o cp.pdf cp.drawio
	open cp.pdf
