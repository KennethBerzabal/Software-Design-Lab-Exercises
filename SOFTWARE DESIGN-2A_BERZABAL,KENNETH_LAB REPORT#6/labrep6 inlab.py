class ButtonDemo(EasyFrame):

    def_init_(self):
        EasyFrame_init_(self)

    var = self.label=self.addlabell(text = "Hello world!",  row = 0, column = 0,  columnspan = 2,  sticky = "NSEW")

    self.clearBtn = self.addButton(text = "Clear",                  row = 1, column = 0)

self.restoreBtn = self.addButton(text="Restore", row=1, column=1, state="disabled")