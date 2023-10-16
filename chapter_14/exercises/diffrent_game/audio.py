from pygame import mixer

class SoundPad:
    """Class for playing sounds while game is running."""
    def __init__(self):
        """Initialize sounds"""
        self.fire_sfx = mixer.Sound('sfx/fire.mp3')
        self.click_sfx = mixer.Sound('sfx/click.mp3')
        self.lvl_up_sfx = mixer.Sound('sfx/lvl_up.mp3')
        self.end_sfx = mixer.Sound('sfx/end.mp3')

        self._set_volume()

    def play(self, sound: str):
        """Playing a choiced sound."""
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
            case _:
                pass

    def stop(self):
        """Stop playing the sound."""
        mixer.stop()

    def _set_volume(self):
        """Adjust the sounds volume."""
        self.fire_sfx.set_volume(0.3)
        self.click_sfx.set_volume(0.4)
        self.end_sfx.set_volume(0.4)
        self.lvl_up_sfx.set_volume(0.2)