WRK_DIR="./temp"

render:
	./generate.py "$(WRK_DIR)/CorePayment.xlsx" | pbcopy

pdf:
	rm -f $(WRK_DIR)/cp.pdf
	./generate.py "$(WRK_DIR)/CorePayment.xlsx" -po landscape > $(WRK_DIR)/cp.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o $(WRK_DIR)/cp.pdf $(WRK_DIR)/cp.drawio
	open $(WRK_DIR)/cp.pdf

ppr:
	rm -f ppr.pdf
	./generate.py "ppr.xlsx" > ppr.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o ppr.pdf ppr.drawio
	open ppr.pdf

bb:
	rm -f bank_binding.pdf
	./generate.py "/Users/huuhoa/Documents/CorePayment/orgchart/BankBinding.xlsx" > bank_binding.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o bank_binding.pdf bank_binding.drawio
	open bank_binding.pdf

status:
	rm -f $(WRK_DIR)/cp_bank_status.pdf
	./generate.py -t status -ps A5 $(WRK_DIR)/CorePayment.xlsx > $(WRK_DIR)/cp_bank_status.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o $(WRK_DIR)/cp_bank_status.pdf $(WRK_DIR)/cp_bank_status.drawio
	open $(WRK_DIR)/cp_bank_status.pdf

status-svg:
	rm -f bank_status.svg
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f svg -o bank_status.svg bank_status.drawio

.PHONY: roadmap
roadmap:
	rm -f $(WRK_DIR)/cp_roadmap.pdf
	./generate.py -t roadmap -ps A5 $(WRK_DIR)/CorePayment.xlsx > $(WRK_DIR)/cp_roadmap.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o $(WRK_DIR)/cp_roadmap.pdf $(WRK_DIR)/cp_roadmap.drawio
	open $(WRK_DIR)/cp_roadmap.pdf

cp:
	./generate.py $(WRK_DIR)/CorePayment.xlsx -po landscape > $(WRK_DIR)/cp_features.drawio
	./generate.py -t status -ps A5 $(WRK_DIR)/CorePayment.xlsx > $(WRK_DIR)/cp_bank_status.drawio
	./generate.py -t roadmap -ps A5 $(WRK_DIR)/CorePayment.xlsx > $(WRK_DIR)/cp_roadmap.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o $(WRK_DIR)/cp_roadmap.pdf $(WRK_DIR)/cp_roadmap.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o $(WRK_DIR)/cp_bank_status.pdf $(WRK_DIR)/cp_bank_status.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o $(WRK_DIR)/cp_features.pdf $(WRK_DIR)/cp_features.drawio

arch:
	rm -f $(WRK_DIR)/cp.pdf
	./generate.py -t arch "$(WRK_DIR)/CorePayment.xlsx" -po landscape > $(WRK_DIR)/cp.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o $(WRK_DIR)/cp.pdf $(WRK_DIR)/cp.drawio
	open $(WRK_DIR)/cp.pdf

arch-test:
	@./generate.py -t arch "$(WRK_DIR)/CorePayment.xlsx" -d True -po landscape

arch-test-1:
	@./generate.py -t arch layout.xlsx -d True -po landscape | ./layout.py -o layout.drawio
	@/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o layout.pdf layout.drawio
	@open layout.pdf

arch-test-2:
	@./generate.py -t arch $(WRK_DIR)/CorePayment.xlsx -d True -po landscape | ./layout.py -o $(WRK_DIR)/layout.drawio
	@/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o $(WRK_DIR)/layout.pdf $(WRK_DIR)/layout.drawio
	@open $(WRK_DIR)/layout.pdf

arch-test-3:
	@./generate.py -e True -o $(WRK_DIR)/layout1.drawio -t arch $(WRK_DIR)/CorePayment.xlsx
	@/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o $(WRK_DIR)/layout1.pdf $(WRK_DIR)/layout1.drawio
	@open $(WRK_DIR)/layout1.pdf

arch-test-4:
	@./generate.py -e True -lt $(WRK_DIR)/layout1.json --write_layout_tree True -o $(WRK_DIR)/layout1.drawio -t arch $(WRK_DIR)/CorePayment.xlsx
	@/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o $(WRK_DIR)/layout-level2.pdf $(WRK_DIR)/layout1.drawio
	@open $(WRK_DIR)/layout-level2.pdf

arch-test-5:
	@./generate.py -ps A3 -e True -lt $(WRK_DIR)/layout1.json --write_layout_tree True -l 1 -o $(WRK_DIR)/layout1.drawio -t arch $(WRK_DIR)/CorePayment.xlsx
	@/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o $(WRK_DIR)/layout-level1.pdf $(WRK_DIR)/layout1.drawio
	@open $(WRK_DIR)/layout-level1.pdf

arch-test-6:
	@./generate.py -ps A4 -po landscape -e True -lt $(WRK_DIR)/layout1.json --write_layout_tree True -l 0 -o $(WRK_DIR)/layout1.drawio -t arch $(WRK_DIR)/CorePayment.xlsx
	@/Applications/draw.io.app/Contents/MacOS/draw.io --export -f pdf -o $(WRK_DIR)/layout-level0.pdf $(WRK_DIR)/layout1.drawio
	@open $(WRK_DIR)/layout-level0.pdf

test:
	python3 tests.py
