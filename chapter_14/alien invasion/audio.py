from pygame import mixer


class SoundPad:
    """Class for playing sounds and music in game."""

    def __init__(self):
        """Initialize the sounds."""
        self.fire_sfx = mixer.Sound('sfx/fire.mp3')
        self.hit_sfx = mixer.Sound('sfx/hit.mp3')
        self.click_sfx = mixer.Sound('sfx/click.mp3')
        self.lvl_up_sfx = mixer.Sound('sfx/lvl_up.mp3')
        self.end_sfx = mixer.Sound('sfx/end.mp3')
        self.minus_life_sfx = mixer.Sound('sfx/minus_life.mp3')

        self.fire_sfx.set_volume(0.3)

    def play(self, sound):
        """Play the choiced sound."""
        match sound:
            case 'fire':
                self.fire_sfx.play()
            case 'hit':
                self.hit_sfx.play()
            case 'click':
                self.click_sfx.play()
            case 'end':
                self.end_sfx.play()
            case 'lvl_up':
                self.lvl_up_sfx.play()
            case 'minus_life':
                self.minus_life_sfx.play()
            case _:
                pass

    def stop(self):
        """Stop playing the sound."""
        mixer.stop()
