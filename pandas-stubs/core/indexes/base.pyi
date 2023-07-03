from collections.abc import (
    Callable,
    Hashable,
    Iterable,
    Iterator,
    Sequence,
)
from typing import (
    ClassVar,
    Generic,
    Literal,
    overload,
)

import numpy as np
from pandas import (
    DataFrame,
    MultiIndex,
    Series,
)
from pandas.core.arrays import ExtensionArray
from pandas.core.base import (
    IndexOpsMixin,
    PandasObject,
)
from pandas.core.strings import StringMethods
from typing_extensions import (
    Never,
    Self,
)

from pandas._typing import (
    S1,
    T1,
    Dtype,
    DtypeArg,
    DtypeObj,
    FillnaOptions,
    HashableT,
    IndexT,
    Label,
    Level,
    NaPosition,
    Scalar,
    np_ndarray_anyint,
    np_ndarray_bool,
    np_ndarray_int64,
    type_t,
)

class InvalidIndexError(Exception): ...

_str = str

class _IndexGetitemMixin(Generic[S1]):
    @overload
    def __getitem__(
        self,
        idx: slice
        | np_ndarray_anyint
        | Sequence[int]
        | Index
        | Series[bool]
        | Sequence[bool]
        | np_ndarray_bool,
    ) -> Self: ...
    @overload
    def __getitem__(self, idx: int) -> S1: ...

class Index(IndexOpsMixin, PandasObject):
    __hash__: ClassVar[None]  # type: ignore[assignment]
    @overload
    def __new__(  # type: ignore[misc]
        cls,
        data: Iterable,
        dtype: Literal["int"] | type_t[int] | type_t[np.integer],
        copy: bool = ...,
        name=...,
        tupleize_cols: bool = ...,
        **kwargs,
    ) -> _IntIndexType: ...
    @overload
    def __new__(  # type: ignore[misc]
        cls,
        data: Iterable,
        dtype: Literal["float"]
        | type_t[float]
        | type_t[np.float32]
        | type_t[np.float64],
        copy: bool = ...,
        name=...,
        tupleize_cols: bool = ...,
        **kwargs,
    ) -> _FloatIndexType: ...
    @overload
    def __new__(  # type: ignore[misc]
        cls,
        data: Iterable,
        dtype: Literal["complex"] | type_t[complex],
        copy: bool = ...,
        name=...,
        tupleize_cols: bool = ...,
        **kwargs,
    ) -> _ComplexIndexType: ...
    @overload
    def __new__(
        cls,
        data: Iterable = ...,
        dtype=...,
        copy: bool = ...,
        name=...,
        tupleize_cols: bool = ...,
        **kwargs,
    ) -> Self: ...
    @property
    def str(self) -> StringMethods[Index, MultiIndex]: ...
    @property
    def asi8(self) -> np_ndarray_int64: ...
    def is_(self, other) -> bool: ...
    def __len__(self) -> int: ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __array_wrap__(self, result, context=...): ...
    @property
    def dtype(self) -> DtypeObj: ...
    def ravel(self, order: _str = ...): ...
    def view(self, cls=...): ...
    def astype(self, dtype: DtypeArg, copy: bool = ...) -> Index: ...
    def take(
        self, indices, axis: int = ..., allow_fill: bool = ..., fill_value=..., **kwargs
    ): ...
    def repeat(self, repeats, axis=...): ...
    def copy(self, name=..., deep: bool = ...) -> Index: ...
    def __copy__(self, **kwargs): ...
    def __deepcopy__(self, memo=...): ...
    def format(
        self, name: bool = ..., formatter: Callable | None = ..., na_rep: _str = ...
    ) -> list[_str]: ...
    def to_native_types(self, slicer=..., **kwargs): ...
    def to_flat_index(self): ...
    def to_series(self, index=..., name=...) -> Series: ...
    def to_frame(self, index: bool = ..., name=...) -> DataFrame: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, value) -> None: ...
    @property
    def names(self) -> list[_str]: ...
    @names.setter
    def names(self, names: list[_str]): ...
    def set_names(self, names, *, level=..., inplace: bool = ...): ...
    def rename(self, name, inplace: bool = ...): ...
    @property
    def nlevels(self) -> int: ...
    def sortlevel(self, level=..., ascending: bool = ..., sort_remaining=...): ...
    def get_level_values(self, level: int | _str) -> Index: ...
    def droplevel(self, level: Level | list[Level] = ...): ...
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    @property
    def is_unique(self) -> bool: ...
    @property
    def has_duplicates(self) -> bool: ...
    def is_boolean(self) -> bool: ...
    def is_integer(self) -> bool: ...
    def is_floating(self) -> bool: ...
    def is_numeric(self) -> bool: ...
    def is_object(self) -> bool: ...
    def is_categorical(self) -> bool: ...
    def is_interval(self) -> bool: ...
    def is_mixed(self) -> bool: ...
    def holds_integer(self): ...
    @property
    def inferred_type(self): ...
    def __reduce__(self): ...
    @property
    def hasnans(self) -> bool: ...
    def isna(self): ...
    isnull = ...
    def notna(self): ...
    notnull = ...
    def fillna(self, value=..., downcast=...): ...
    def dropna(self, how: Literal["any", "all"] = ...) -> Index: ...
    def unique(self, level=...) -> Index: ...
    def drop_duplicates(
        self, *, keep: NaPosition | Literal[False] = ...
    ) -> IndexOpsMixin: ...
    def duplicated(
        self, keep: Literal["first", "last", False] = ...
    ) -> np_ndarray_bool: ...
    def __and__(self, other: Never) -> Never: ...
    def __rand__(self, other: Never) -> Never: ...
    def __or__(self, other: Never) -> Never: ...
    def __ror__(self, other: Never) -> Never: ...
    def __xor__(self, other: Never) -> Never: ...
    def __rxor__(self, other: Never) -> Never: ...
    def __neg__(self: IndexT) -> IndexT: ...
    def __nonzero__(self) -> None: ...
    __bool__ = ...
    def union(self, other: list[HashableT] | Index, sort=...) -> Index: ...
    def intersection(self, other: list[T1] | Index, sort: bool = ...) -> Index: ...
    def difference(self, other: list | Index, sort: bool | None = None) -> Index: ...
    def symmetric_difference(
        self, other: list[T1] | Index, result_name=..., sort=...
    ) -> Index: ...
    def get_loc(
        self,
        key: Label,
        method: FillnaOptions | Literal["nearest"] | None = ...,
        tolerance=...,
    ): ...
    def get_indexer(self, target, method=..., limit=..., tolerance=...): ...
    def reindex(self, target, method=..., level=..., limit=..., tolerance=...): ...
    def join(
        self,
        other,
        *,
        how: _str = ...,
        level=...,
        return_indexers: bool = ...,
        sort: bool = ...,
    ): ...
    @property
    def values(self) -> np.ndarray: ...
    @property
    def array(self) -> ExtensionArray: ...
    def memory_usage(self, deep: bool = ...): ...
    def where(self, cond, other=...): ...
    def is_type_compatible(self, kind) -> bool: ...
    def __contains__(self, key) -> bool: ...
    def __setitem__(self, key, value) -> None: ...
    @overload
    def __getitem__(
        self: IndexT,
        idx: slice
        | np_ndarray_anyint
        | Sequence[int]
        | Index
        | Series[bool]
        | Sequence[bool]
        | np_ndarray_bool,
    ) -> IndexT: ...
    @overload
    def __getitem__(self, idx: int | tuple[np_ndarray_anyint, ...]) -> Scalar: ...
    def append(self, other): ...
    def putmask(self, mask, value): ...
    def equals(self, other) -> bool: ...
    def identical(self, other) -> bool: ...
    def asof(self, label): ...
    def asof_locs(self, where, mask): ...
    def sort_values(self, return_indexer: bool = ..., ascending: bool = ...): ...
    def sort(self, *args, **kwargs) -> None: ...
    def shift(self, periods: int = ..., freq=...) -> None: ...
    def argsort(self, *args, **kwargs): ...
    def get_value(self, series, key): ...
    def set_value(self, arr, key, value) -> None: ...
    def get_indexer_non_unique(self, target): ...
    def get_indexer_for(self, target, **kwargs): ...
    def groupby(self, values) -> dict[Hashable, np.ndarray]: ...
    def map(self, mapper, na_action=...) -> Index: ...
    def isin(self, values, level=...) -> np_ndarray_bool: ...
    def slice_indexer(self, start=..., end=..., step=...): ...
    def get_slice_bound(self, label, side): ...
    def slice_locs(self, start=..., end=..., step=...): ...
    def delete(self, loc): ...
    def insert(self, loc, item): ...
    def drop(self, labels, errors: _str = ...) -> Index: ...
    @property
    def shape(self) -> tuple[int, ...]: ...
    # Extra methods from old stubs
    def __eq__(self, other: object) -> np_ndarray_bool: ...  # type: ignore[override]
    def __iter__(self) -> Iterator: ...
    def __ne__(self, other: object) -> np_ndarray_bool: ...  # type: ignore[override]
    def __le__(self, other: Index | Scalar) -> np_ndarray_bool: ...  # type: ignore[override]
    def __ge__(self, other: Index | Scalar) -> np_ndarray_bool: ...  # type: ignore[override]
    def __lt__(self, other: Index | Scalar) -> np_ndarray_bool: ...  # type: ignore[override]
    def __gt__(self, other: Index | Scalar) -> np_ndarray_bool: ...  # type: ignore[override]

def ensure_index_from_sequences(
    sequences: Sequence[Sequence[Dtype]], names: list[str] = ...
) -> Index: ...
def ensure_index(index_like: Sequence | Index, copy: bool = ...) -> Index: ...
def maybe_extract_name(name, obj, cls) -> Label: ...

class _NumericIndexType(Index):
    def __add__(self, other: _NumericIndexType | complex) -> Self: ...
    def __radd__(self, other: _NumericIndexType | complex) -> Self: ...
    def __sub__(self, other: _NumericIndexType | complex) -> Self: ...
    def __rsub__(self, other: _NumericIndexType | complex) -> Self: ...
    def __mul__(self, other: _NumericIndexType | complex) -> Self: ...
    def __rmul__(self, other: _NumericIndexType | complex) -> Self: ...
    def __truediv__(self, other: _NumericIndexType | complex) -> Self: ...
    def __rtruediv__(self, other: _NumericIndexType | complex) -> Self: ...
    def __floordiv__(self, other: _NumericIndexType | complex) -> Self: ...
    def __rfloordiv__(self, other: _NumericIndexType | complex) -> Self: ...

class _FloatIndexType(_NumericIndexType): ...
class _IntIndexType(_NumericIndexType): ...
class _ComplexIndexType(_NumericIndexType): ...
