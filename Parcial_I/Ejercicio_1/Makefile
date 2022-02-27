COMPILAR = kotlinc
KFLAG	 = -cp
OBJDIR   = archivosO
OBJETOS  = $(OBJDIR)/FunctionsKt.class $(OBJDIR)/MainKt.class

all: $(OBJETOS)

clean:
	rmdir $(OBJDIR)

run: 
	( cd $(OBJDIR) ; kotlin MainKt )

$(OBJDIR)/FunctionsKt.class: Functions.kt
	$(COMPILAR) Functions.kt -d $(OBJDIR)

$(OBJDIR)/MainKt.class: $(OBJDIR)/FunctionsKt.class Main.kt
	$(COMPILAR) $(KFLAG) $(OBJDIR)/. Main.kt -d $(OBJDIR)

$(OBJDIR):
	mkdir $(OBJDIR)
