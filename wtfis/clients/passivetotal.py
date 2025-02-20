from typing import Optional

from wtfis.clients.base import BaseClient
from wtfis.models.passivetotal import Whois
from wtfis.utils import refang


class PTClient(BaseClient):
    """
    Passivetotal client
    """
    baseurl = "https://api.riskiq.net/pt/v2"

    def __init__(self, api_user: str, api_key: str) -> None:
        super().__init__()
        self.s.auth = (api_user, api_key)

    def _query(self, path: str, query: str) -> Optional[dict]:
        return self._get(
            path,
            params={"query": query}
        )

    def get_passive_dns(self, domain: str) -> Optional[dict]:
        return self._query("/dns/passive", refang(domain))

    def get_whois(self, entity: str) -> Optional[Whois]:
        return Whois.parse_obj(self._query("/whois", refang(entity)))
