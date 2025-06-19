import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
import homeassistant.helpers.config_validation as cv

DOMAIN = 'news_feed_reader'

FEEDS = {
    'ynet_main': 'https://www.ynet.co.il/Integration/StoryRss1854.xml',
    'ynet_sport': 'https://www.ynet.co.il/Integration/StoryRss3.xml',
    'maariv': 'https://www.maariv.co.il/Rss/RssFeedsMivzakiChadashot',
    'walla': 'https://rss.walla.co.il/feed/22',
    'themarker': 'https://www.themarker.com/srv/tm-markets'
}

class NewsFeedConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title='News Feeds', data=user_input)

        options_schema = vol.Schema({
            vol.Required(feed, default=True): bool for feed in FEEDS
        })
        return self.async_show_form(step_id='user', data_schema=options_schema, errors=errors)
