"""Pipedrive destination: search by match_field, then create or update (#1183).

Work in progress: load() is not implemented yet.
"""

from __future__ import annotations

from typing import Any

from drt.config.models import DestinationConfig, PipedriveDestinationConfig, SyncOptions
from drt.destinations.base import SyncResult


class PipedriveDestination:
    def load(
        self,
        records: list[dict[str, Any]],
        config: DestinationConfig,
        sync_options: SyncOptions,
    ) -> SyncResult:
        assert isinstance(config, PipedriveDestinationConfig)
        if not records:
            return SyncResult()
        raise NotImplementedError("Pipedrive destination: load() is not implemented yet.")
