.PHONY: all crayola clean nuke

PALETTES=$(shell find palette -type f)
FORMATTED=$(patsubst palette/%.colors,palette/%.ini,$(PALETTES))
TOOLBARS_LEFT=$(patsubst palette/%.colors,toolbar/left-handed/%.ini,$(PALETTES))
TOOLBARS_RIGHT=$(patsubst palette/%.colors,toolbar/right-handed/%.ini,$(PALETTES))
TOOLBARS=$(TOOLBARS_LEFT) $(TOOLBARS_RIGHT)

all: $(TOOLBARS)

crayola:
	mkdir -p palette
	curl 'https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors' | python wikipedia-tables-extract.py

palette/%.ini: palette/%.colors
	python3 sort.py < $< | uniq | python3 format-xournalpp.py 2 > $@

toolbar/left-handed/%.ini: palette/%.ini palette/%.title
	mkdir -p $(dir $@)
	xargs -d'\n' -a $< < toolbar.ini tmpl --title "Left hand note Taking with Crayola's $(shell cat $(word 2,$^))" --side Right --cols | sed 's/,$$//' > $@

toolbar/right-handed/%.ini: palette/%.ini palette/%.title
	mkdir -p $(dir $@)
	xargs -d'\n' -a $< < toolbar.ini tmpl --title "Right hand note Taking with Crayola's $(shell cat $(word 2,$^))" --side Left --cols | sed 's/,$$//' > $@

clean:
	rm -rf toolbar

nuke: clean
	rm -rf palette
