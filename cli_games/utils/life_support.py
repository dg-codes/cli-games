from dataclasses import dataclass


@dataclass
class LivesDisplay:
    available: str = "❤️"
    missing: str = "🖤"


class LifeSupport:
    def __init__(self, total_lives):
        self.lives_total = total_lives
        self.lives_lost = 0
        self.lives_left = total_lives
        self.is_dead = False
        self.display = LivesDisplay()
        self.display_lives()

    def manage_hit(self):
        if self.is_dead:
            return

        self.lives_lost += 1
        self.lives_left -= 1
        self.display_lives()

        if self.lives_left == 0:
            self.is_dead = True
            self._display_dead()

        return self.lives_left

    def display_lives(self):
        _display_message = (
            self.display.available * self.lives_left
            + self.display.missing * self.lives_lost
        )
        print(_display_message, "\n")
        return _display_message

    def _display_dead(self):
        _message = "💀  You be dead now mon! 💀"
        print(_message)
        return _message
