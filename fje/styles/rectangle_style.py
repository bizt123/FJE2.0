# fje/styles/rectangle_style.py
from .style_interface import IStyle


class RectangleStyle(IStyle):
    RectangleLength = 40
    Outstream = []

    def draw(self, component):
        if component.level == "root":
            return
        outstr = (
            (len(component.level) - 1) * "│  " + "├─" + component.icon + component.name
        ) + " "
        if len(outstr) + 1 < self.RectangleLength:
            outstr += "─" * (self.RectangleLength - (len(outstr) + 1))
        else:
            self.RectangleLength = len(outstr) + 1
        outstr += "┤"
        self.Outstream.append(outstr)
        if component.level[-1] == "r" and component.is_container == False:
            pos = outstr.find("├")
            outstr = outstr[:pos].replace(" ", "─").replace("│", "┴") + outstr[
                pos:
            ].replace("├", "┴").replace("┤", "┘")
            outstr = "└" + outstr[1:]
            self.Outstream[0] = self.Outstream[0].replace("├", "┌").replace("┤", "┐")
            self.Outstream[-1] = outstr

            self.upd_length(self, self.RectangleLength)
            print("\n".join(self.Outstream))
            self.Outstream = []

    def upd_length(self, new_length):
        if self.RectangleLength <= new_length:
            for i, outstr in enumerate(self.Outstream):
                delta = new_length - len(outstr)
                self.Outstream[i] = outstr[:-1] + "─" * delta + outstr[-1]
            self.RectangleLength = new_length

    def change_front(self, prefix, id, num_children):
        prefix_child = ""
        if prefix == "root":
            if id + 1 == num_children:
                prefix_child = "r"
            else:
                prefix_child = "m"
        elif prefix[-1] == "r" and id + 1 == num_children:
            prefix_child = prefix + "r"
        else:
            prefix_child = prefix + "m"
        return prefix_child
