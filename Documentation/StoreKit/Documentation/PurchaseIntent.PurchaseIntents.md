Instance Method

# makeAsyncIterator()

Creates the iterator that produces elements of the asynchronous sequence.

iOS 16.4+  iPadOS 16.4+  macOS 14.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    func makeAsyncIterator() -> PurchaseIntent.PurchaseIntents.AsyncIterator

## Relationships

### From Protocol

  * `AsyncSequence`

## See Also

### Iterating over purchase intents

`struct PurchaseIntent.PurchaseIntents.AsyncIterator`

An iterator that produces elements of the asynchronous purchase intents
sequence.

`typealias PurchaseIntent.PurchaseIntents.Element`

A type that represents a purchase intents element.

Type Alias

# PurchaseIntent.PurchaseIntents.Element

A type that represents a purchase intents element.

iOS 16.4+  iPadOS 16.4+  macOS 14.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    typealias PurchaseIntent.PurchaseIntents.Element = PurchaseIntent

## See Also

### Iterating over purchase intents

`func makeAsyncIterator() -> PurchaseIntent.PurchaseIntents.AsyncIterator`

Creates the iterator that produces elements of the asynchronous sequence.

`struct PurchaseIntent.PurchaseIntents.AsyncIterator`

An iterator that produces elements of the asynchronous purchase intents
sequence.

Instance Method

# allSatisfy(_:)

Returns a Boolean value that indicates whether all elements produced by the
asynchronous sequence satisfy the given predicate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    func allSatisfy(_ predicate: (PurchaseIntent) async throws -> Bool) async rethrows -> Bool

##  Parameters

`predicate`

    

A closure that takes an element of the asynchronous sequence as its argument
and returns a Boolean value that indicates whether the passed element
satisfies a condition.

## Return Value

`true` if the sequence contains only elements that satisfy `predicate`;
otherwise, `false`.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `10`. The `allSatisfy(_:)` method checks to see whether all
elements produced by the sequence are less than `10`.

The predicate executes each time the asynchronous sequence produces an
element, until either the predicate returns `false` or the sequence ends.

If the asynchronous sequence is empty, this method returns `true`.

## See Also

### Filtering and matching purchase intents

`func contains(PurchaseIntent) -> Bool`

Returns a Boolean value that indicates whether the asynchronous sequence
contains the given element.

`func contains(where: (PurchaseIntent) -> Bool) -> Bool`

Returns a Boolean value that indicates whether the asynchronous sequence
contains an element that satisfies the given predicate.

`func filter((PurchaseIntent) -> Bool) ->
AsyncFilterSequence<PurchaseIntent.PurchaseIntents>`

Creates an asynchronous sequence that contains, in order, the elements of the
base sequence that satisfy the given predicate.

`func first(where: (PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the first element of the sequence that satisfies the given predicate.

`func max(by: (PurchaseIntent, PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the maximum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

`func min(by: (PurchaseIntent, PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the minimum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

Instance Method

# contains(_:)

Returns a Boolean value that indicates whether the asynchronous sequence
contains the given element.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    func contains(_ search: PurchaseIntent) async rethrows -> Bool

##  Parameters

`search`

    

The element to find in the asynchronous sequence.

## Return Value

`true` if the method found the element in the asynchronous sequence;
otherwise, `false`.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `10`. The `contains(_:)` method checks to see whether the
sequence produces the value `5`:

## See Also

### Filtering and matching purchase intents

`func allSatisfy((PurchaseIntent) -> Bool) -> Bool`

Returns a Boolean value that indicates whether all elements produced by the
asynchronous sequence satisfy the given predicate.

`func contains(where: (PurchaseIntent) -> Bool) -> Bool`

Returns a Boolean value that indicates whether the asynchronous sequence
contains an element that satisfies the given predicate.

`func filter((PurchaseIntent) -> Bool) ->
AsyncFilterSequence<PurchaseIntent.PurchaseIntents>`

Creates an asynchronous sequence that contains, in order, the elements of the
base sequence that satisfy the given predicate.

`func first(where: (PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the first element of the sequence that satisfies the given predicate.

`func max(by: (PurchaseIntent, PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the maximum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

`func min(by: (PurchaseIntent, PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the minimum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

Instance Method

# contains(where:)

Returns a Boolean value that indicates whether the asynchronous sequence
contains an element that satisfies the given predicate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    func contains(where predicate: (PurchaseIntent) async throws -> Bool) async rethrows -> Bool

##  Parameters

`predicate`

    

A closure that takes an element of the asynchronous sequence as its argument
and returns a Boolean value that indicates whether the passed element
represents a match.

## Return Value

`true` if the sequence contains an element that satisfies predicate;
otherwise, `false`.

## Discussion

You can use the predicate to check for an element of a type that doesn’t
conform to the `Equatable` protocol, or to find an element that satisfies a
general condition.

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `10`. The `contains(where:)` method checks to see whether
the sequence produces a value divisible by `3`:

The predicate executes each time the asynchronous sequence produces an
element, until either the predicate finds a match or the sequence ends.

## See Also

### Filtering and matching purchase intents

`func allSatisfy((PurchaseIntent) -> Bool) -> Bool`

Returns a Boolean value that indicates whether all elements produced by the
asynchronous sequence satisfy the given predicate.

`func contains(PurchaseIntent) -> Bool`

Returns a Boolean value that indicates whether the asynchronous sequence
contains the given element.

`func filter((PurchaseIntent) -> Bool) ->
AsyncFilterSequence<PurchaseIntent.PurchaseIntents>`

Creates an asynchronous sequence that contains, in order, the elements of the
base sequence that satisfy the given predicate.

`func first(where: (PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the first element of the sequence that satisfies the given predicate.

`func max(by: (PurchaseIntent, PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the maximum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

`func min(by: (PurchaseIntent, PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the minimum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

Instance Method

# filter(_:)

Creates an asynchronous sequence that contains, in order, the elements of the
base sequence that satisfy the given predicate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    @preconcurrency
    func filter(_ isIncluded: @escaping @Sendable (PurchaseIntent) async -> Bool) -> AsyncFilterSequence<PurchaseIntent.PurchaseIntents>

##  Parameters

`isIncluded`

    

A closure that takes an element of the asynchronous sequence as its argument
and returns a Boolean value that indicates whether to include the element in
the filtered sequence.

## Return Value

An asynchronous sequence that contains, in order, the elements of the base
sequence that satisfy the given predicate.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `10`. The `filter(_:)` method returns `true` for even
values and `false` for odd values, thereby filtering out the odd values:

## See Also

### Filtering and matching purchase intents

`func allSatisfy((PurchaseIntent) -> Bool) -> Bool`

Returns a Boolean value that indicates whether all elements produced by the
asynchronous sequence satisfy the given predicate.

`func contains(PurchaseIntent) -> Bool`

Returns a Boolean value that indicates whether the asynchronous sequence
contains the given element.

`func contains(where: (PurchaseIntent) -> Bool) -> Bool`

Returns a Boolean value that indicates whether the asynchronous sequence
contains an element that satisfies the given predicate.

`func first(where: (PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the first element of the sequence that satisfies the given predicate.

`func max(by: (PurchaseIntent, PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the maximum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

`func min(by: (PurchaseIntent, PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the minimum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

Instance Method

# first(where:)

Returns the first element of the sequence that satisfies the given predicate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    func first(where predicate: (PurchaseIntent) async throws -> Bool) async rethrows -> PurchaseIntent?

##  Parameters

`predicate`

    

A closure that takes an element of the asynchronous sequence as its argument
and returns a Boolean value that indicates whether the element is a match.

## Return Value

The first element of the sequence that satisfies `predicate`, or `nil` if
there is no element that satisfies `predicate`.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `10`. The `first(where:)` method returns the first member
of the sequence that’s evenly divisible by both `2` and `3`.

The predicate executes each time the asynchronous sequence produces an
element, until either the predicate finds a match or the sequence ends.

## See Also

### Filtering and matching purchase intents

`func allSatisfy((PurchaseIntent) -> Bool) -> Bool`

Returns a Boolean value that indicates whether all elements produced by the
asynchronous sequence satisfy the given predicate.

`func contains(PurchaseIntent) -> Bool`

Returns a Boolean value that indicates whether the asynchronous sequence
contains the given element.

`func contains(where: (PurchaseIntent) -> Bool) -> Bool`

Returns a Boolean value that indicates whether the asynchronous sequence
contains an element that satisfies the given predicate.

`func filter((PurchaseIntent) -> Bool) ->
AsyncFilterSequence<PurchaseIntent.PurchaseIntents>`

Creates an asynchronous sequence that contains, in order, the elements of the
base sequence that satisfy the given predicate.

`func max(by: (PurchaseIntent, PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the maximum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

`func min(by: (PurchaseIntent, PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the minimum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

Instance Method

# max(by:)

Returns the maximum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    @warn_unqualified_access
    func max(by areInIncreasingOrder: (PurchaseIntent, PurchaseIntent) async throws -> Bool) async rethrows -> PurchaseIntent?

##  Parameters

`areInIncreasingOrder`

    

A predicate that returns `true` if its first argument should be ordered before
its second argument; otherwise, `false`.

## Return Value

The sequence’s minimum element, according to `areInIncreasingOrder`. If the
sequence has no elements, returns `nil`.

## Discussion

Use this method when the asynchronous sequence’s values don’t conform to
`Comparable`, or when you want to apply a custom ordering to the sequence.

The predicate must be a _strict weak ordering_ over the elements. That is, for
any elements `a`, `b`, and `c`, the following conditions must hold:

  * `areInIncreasingOrder(a, a)` is always `false`. (Irreflexivity)

  * If `areInIncreasingOrder(a, b)` and `areInIncreasingOrder(b, c)` are both `true`, then `areInIncreasingOrder(a, c)` is also `true`. (Transitive comparability)

  * Two elements are _incomparable_ if neither is ordered before the other according to the predicate. If `a` and `b` are incomparable, and `b` and `c` are incomparable, then `a` and `c` are also incomparable. (Transitive incomparability)

The following example uses an enumeration of playing cards ranks, `Rank`,
which ranges from `ace` (low) to `king` (high). An asynchronous sequence
called `RankCounter` produces all elements of the array. The predicate
provided to the `max(by:)` method sorts ranks based on their `rawValue`:

## See Also

### Filtering and matching purchase intents

`func allSatisfy((PurchaseIntent) -> Bool) -> Bool`

Returns a Boolean value that indicates whether all elements produced by the
asynchronous sequence satisfy the given predicate.

`func contains(PurchaseIntent) -> Bool`

Returns a Boolean value that indicates whether the asynchronous sequence
contains the given element.

`func contains(where: (PurchaseIntent) -> Bool) -> Bool`

Returns a Boolean value that indicates whether the asynchronous sequence
contains an element that satisfies the given predicate.

`func filter((PurchaseIntent) -> Bool) ->
AsyncFilterSequence<PurchaseIntent.PurchaseIntents>`

Creates an asynchronous sequence that contains, in order, the elements of the
base sequence that satisfy the given predicate.

`func first(where: (PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the first element of the sequence that satisfies the given predicate.

`func min(by: (PurchaseIntent, PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the minimum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

Instance Method

# min(by:)

Returns the minimum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    @warn_unqualified_access
    func min(by areInIncreasingOrder: (PurchaseIntent, PurchaseIntent) async throws -> Bool) async rethrows -> PurchaseIntent?

##  Parameters

`areInIncreasingOrder`

    

A predicate that returns `true` if its first argument should be ordered before
its second argument; otherwise, `false`.

## Return Value

The sequence’s minimum element, according to `areInIncreasingOrder`. If the
sequence has no elements, returns `nil`.

## Discussion

Use this method when the asynchronous sequence’s values don’t conform to
`Comparable`, or when you want to apply a custom ordering to the sequence.

The predicate must be a _strict weak ordering_ over the elements. That is, for
any elements `a`, `b`, and `c`, the following conditions must hold:

  * `areInIncreasingOrder(a, a)` is always `false`. (Irreflexivity)

  * If `areInIncreasingOrder(a, b)` and `areInIncreasingOrder(b, c)` are both `true`, then `areInIncreasingOrder(a, c)` is also `true`. (Transitive comparability)

  * Two elements are _incomparable_ if neither is ordered before the other according to the predicate. If `a` and `b` are incomparable, and `b` and `c` are incomparable, then `a` and `c` are also incomparable. (Transitive incomparability)

The following example uses an enumeration of playing cards ranks, `Rank`,
which ranges from `ace` (low) to `king` (high). An asynchronous sequence
called `RankCounter` produces all elements of the array. The predicate
provided to the `min(by:)` method sorts ranks based on their `rawValue`:

## See Also

### Filtering and matching purchase intents

`func allSatisfy((PurchaseIntent) -> Bool) -> Bool`

Returns a Boolean value that indicates whether all elements produced by the
asynchronous sequence satisfy the given predicate.

`func contains(PurchaseIntent) -> Bool`

Returns a Boolean value that indicates whether the asynchronous sequence
contains the given element.

`func contains(where: (PurchaseIntent) -> Bool) -> Bool`

Returns a Boolean value that indicates whether the asynchronous sequence
contains an element that satisfies the given predicate.

`func filter((PurchaseIntent) -> Bool) ->
AsyncFilterSequence<PurchaseIntent.PurchaseIntents>`

Creates an asynchronous sequence that contains, in order, the elements of the
base sequence that satisfy the given predicate.

`func first(where: (PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the first element of the sequence that satisfies the given predicate.

`func max(by: (PurchaseIntent, PurchaseIntent) -> Bool) -> PurchaseIntent?`

Returns the maximum element in the asynchronous sequence, using the given
predicate as the comparison between elements.

Generic Instance Method

# compactMap(_:)

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements, omitting results that don’t return a value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    @preconcurrency
    func compactMap<ElementOfResult>(_ transform: @escaping @Sendable (PurchaseIntent) async -> ElementOfResult?) -> AsyncCompactMapSequence<PurchaseIntent.PurchaseIntents, ElementOfResult>

##  Parameters

`transform`

    

A mapping closure. `transform` accepts an element of this sequence as its
parameter and returns a transformed value of the same or of a different type.

## Return Value

An asynchronous sequence that contains, in order, the non-`nil` elements
produced by the `transform` closure.

## Discussion

Use the `compactMap(_:)` method to transform every element received from a
base asynchronous sequence, while also discarding any `nil` results from the
closure. Typically, you use this to transform from one type of element to
another.

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `5`. The closure provided to the `compactMap(_:)` method
takes each `Int` and looks up a corresponding `String` from a
`romanNumeralDict` dictionary. Because there is no key for `4`, the closure
returns `nil` in this case, which `compactMap(_:)` omits from the transformed
asynchronous sequence.

## See Also

### Transforming purchase intents

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncThrowingCompactMapSequence<PurchaseIntent.PurchaseIntents,
ElementOfResult>`

Creates an asynchronous sequence that maps an error-throwing closure over the
base sequence’s elements, omitting results that don’t return a value.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncThrowingFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given error-throwing transformation with each element of this sequence.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given transformation with each element of this sequence.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncThrowingMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given error-throwing closure
over the asynchronous sequence’s elements.

`func prefix(Int) -> AsyncPrefixSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, up to the specified maximum length,
containing the initial elements of the base asynchronous sequence.

`func prefix(while: (PurchaseIntent) -> Bool) ->
AsyncPrefixWhileSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, containing the initial, consecutive elements
of the base sequence that satisfy the given predicate.

`func reduce<Result>(Result, (Result, PurchaseIntent) -> Result) -> Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure.

`func reduce<Result>(into: Result, (inout Result, PurchaseIntent) -> Void) ->
Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure, given a mutable initial value.

Generic Instance Method

# compactMap(_:)

Creates an asynchronous sequence that maps an error-throwing closure over the
base sequence’s elements, omitting results that don’t return a value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    @preconcurrency
    func compactMap<ElementOfResult>(_ transform: @escaping @Sendable (PurchaseIntent) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<PurchaseIntent.PurchaseIntents, ElementOfResult>

##  Parameters

`transform`

    

An error-throwing mapping closure. `transform` accepts an element of this
sequence as its parameter and returns a transformed value of the same or of a
different type. If `transform` throws an error, the sequence ends.

## Return Value

An asynchronous sequence that contains, in order, the non-`nil` elements
produced by the `transform` closure. The sequence ends either when the base
sequence ends or when `transform` throws an error.

## Discussion

Use the `compactMap(_:)` method to transform every element received from a
base asynchronous sequence, while also discarding any `nil` results from the
closure. Typically, you use this to transform from one type of element to
another.

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `5`. The closure provided to the `compactMap(_:)` method
takes each `Int` and looks up a corresponding `String` from a
`romanNumeralDict` dictionary. Since there is no key for `4`, the closure
returns `nil` in this case, which `compactMap(_:)` omits from the transformed
asynchronous sequence. When the value is `5`, the closure throws `MyError`,
terminating the sequence.

## See Also

### Transforming purchase intents

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncCompactMapSequence<PurchaseIntent.PurchaseIntents, ElementOfResult>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements, omitting results that don’t return a value.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncThrowingFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given error-throwing transformation with each element of this sequence.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given transformation with each element of this sequence.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncThrowingMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given error-throwing closure
over the asynchronous sequence’s elements.

`func prefix(Int) -> AsyncPrefixSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, up to the specified maximum length,
containing the initial elements of the base asynchronous sequence.

`func prefix(while: (PurchaseIntent) -> Bool) ->
AsyncPrefixWhileSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, containing the initial, consecutive elements
of the base sequence that satisfy the given predicate.

`func reduce<Result>(Result, (Result, PurchaseIntent) -> Result) -> Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure.

`func reduce<Result>(into: Result, (inout Result, PurchaseIntent) -> Void) ->
Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure, given a mutable initial value.

Generic Instance Method

# flatMap(_:)

Creates an asynchronous sequence that concatenates the results of calling the
given error-throwing transformation with each element of this sequence.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    @preconcurrency
    func flatMap<SegmentOfResult>(_ transform: @escaping @Sendable (PurchaseIntent) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult> where SegmentOfResult : AsyncSequence

##  Parameters

`transform`

    

An error-throwing mapping closure. `transform` accepts an element of this
sequence as its parameter and returns an `AsyncSequence`. If `transform`
throws an error, the sequence ends.

## Return Value

A single, flattened asynchronous sequence that contains all elements in all
the asynchronous sequences produced by `transform`. The sequence ends either
when the last sequence created from the last element from base sequence ends,
or when `transform` throws an error.

## Discussion

Use this method to receive a single-level asynchronous sequence when your
transformation produces an asynchronous sequence for each element.

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `5`. The transforming closure takes the received `Int` and
returns a new `Counter` that counts that high. For example, when the transform
receives `3` from the base sequence, it creates a new `Counter` that produces
the values `1`, `2`, and `3`. The `flatMap(_:)` method “flattens” the
resulting sequence-of-sequences into a single `AsyncSequence`. However, when
the closure receives `4`, it throws an error, terminating the sequence.

## See Also

### Transforming purchase intents

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncCompactMapSequence<PurchaseIntent.PurchaseIntents, ElementOfResult>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements, omitting results that don’t return a value.

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncThrowingCompactMapSequence<PurchaseIntent.PurchaseIntents,
ElementOfResult>`

Creates an asynchronous sequence that maps an error-throwing closure over the
base sequence’s elements, omitting results that don’t return a value.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given transformation with each element of this sequence.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncThrowingMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given error-throwing closure
over the asynchronous sequence’s elements.

`func prefix(Int) -> AsyncPrefixSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, up to the specified maximum length,
containing the initial elements of the base asynchronous sequence.

`func prefix(while: (PurchaseIntent) -> Bool) ->
AsyncPrefixWhileSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, containing the initial, consecutive elements
of the base sequence that satisfy the given predicate.

`func reduce<Result>(Result, (Result, PurchaseIntent) -> Result) -> Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure.

`func reduce<Result>(into: Result, (inout Result, PurchaseIntent) -> Void) ->
Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure, given a mutable initial value.

Generic Instance Method

# flatMap(_:)

Creates an asynchronous sequence that concatenates the results of calling the
given transformation with each element of this sequence.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    @preconcurrency
    func flatMap<SegmentOfResult>(_ transform: @escaping @Sendable (PurchaseIntent) async -> SegmentOfResult) -> AsyncFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult> where SegmentOfResult : AsyncSequence

##  Parameters

`transform`

    

A mapping closure. `transform` accepts an element of this sequence as its
parameter and returns an `AsyncSequence`.

## Return Value

A single, flattened asynchronous sequence that contains all elements in all
the asynchronous sequences produced by `transform`.

## Discussion

Use this method to receive a single-level asynchronous sequence when your
transformation produces an asynchronous sequence for each element.

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `5`. The transforming closure takes the received `Int` and
returns a new `Counter` that counts that high. For example, when the transform
receives `3` from the base sequence, it creates a new `Counter` that produces
the values `1`, `2`, and `3`. The `flatMap(_:)` method “flattens” the
resulting sequence-of-sequences into a single `AsyncSequence`.

## See Also

### Transforming purchase intents

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncCompactMapSequence<PurchaseIntent.PurchaseIntents, ElementOfResult>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements, omitting results that don’t return a value.

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncThrowingCompactMapSequence<PurchaseIntent.PurchaseIntents,
ElementOfResult>`

Creates an asynchronous sequence that maps an error-throwing closure over the
base sequence’s elements, omitting results that don’t return a value.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncThrowingFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given error-throwing transformation with each element of this sequence.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncThrowingMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given error-throwing closure
over the asynchronous sequence’s elements.

`func prefix(Int) -> AsyncPrefixSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, up to the specified maximum length,
containing the initial elements of the base asynchronous sequence.

`func prefix(while: (PurchaseIntent) -> Bool) ->
AsyncPrefixWhileSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, containing the initial, consecutive elements
of the base sequence that satisfy the given predicate.

`func reduce<Result>(Result, (Result, PurchaseIntent) -> Result) -> Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure.

`func reduce<Result>(into: Result, (inout Result, PurchaseIntent) -> Void) ->
Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure, given a mutable initial value.

Generic Instance Method

# map(_:)

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    @preconcurrency
    func map<Transformed>(_ transform: @escaping @Sendable (PurchaseIntent) async -> Transformed) -> AsyncMapSequence<PurchaseIntent.PurchaseIntents, Transformed>

##  Parameters

`transform`

    

A mapping closure. `transform` accepts an element of this sequence as its
parameter and returns a transformed value of the same or of a different type.

## Return Value

An asynchronous sequence that contains, in order, the elements produced by the
`transform` closure.

## Discussion

Use the `map(_:)` method to transform every element received from a base
asynchronous sequence. Typically, you use this to transform from one type of
element to another.

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `5`. The closure provided to the `map(_:)` method takes
each `Int` and looks up a corresponding `String` from a `romanNumeralDict`
dictionary. This means the outer `for await in` loop iterates over `String`
instances instead of the underlying `Int` values that `Counter` produces:

## See Also

### Transforming purchase intents

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncCompactMapSequence<PurchaseIntent.PurchaseIntents, ElementOfResult>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements, omitting results that don’t return a value.

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncThrowingCompactMapSequence<PurchaseIntent.PurchaseIntents,
ElementOfResult>`

Creates an asynchronous sequence that maps an error-throwing closure over the
base sequence’s elements, omitting results that don’t return a value.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncThrowingFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given error-throwing transformation with each element of this sequence.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given transformation with each element of this sequence.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncThrowingMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given error-throwing closure
over the asynchronous sequence’s elements.

`func prefix(Int) -> AsyncPrefixSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, up to the specified maximum length,
containing the initial elements of the base asynchronous sequence.

`func prefix(while: (PurchaseIntent) -> Bool) ->
AsyncPrefixWhileSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, containing the initial, consecutive elements
of the base sequence that satisfy the given predicate.

`func reduce<Result>(Result, (Result, PurchaseIntent) -> Result) -> Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure.

`func reduce<Result>(into: Result, (inout Result, PurchaseIntent) -> Void) ->
Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure, given a mutable initial value.

Generic Instance Method

# map(_:)

Creates an asynchronous sequence that maps the given error-throwing closure
over the asynchronous sequence’s elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    @preconcurrency
    func map<Transformed>(_ transform: @escaping @Sendable (PurchaseIntent) async throws -> Transformed) -> AsyncThrowingMapSequence<PurchaseIntent.PurchaseIntents, Transformed>

##  Parameters

`transform`

    

A mapping closure. `transform` accepts an element of this sequence as its
parameter and returns a transformed value of the same or of a different type.
`transform` can also throw an error, which ends the transformed sequence.

## Return Value

An asynchronous sequence that contains, in order, the elements produced by the
`transform` closure.

## Discussion

Use the `map(_:)` method to transform every element received from a base
asynchronous sequence. Typically, you use this to transform from one type of
element to another.

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `5`. The closure provided to the `map(_:)` method takes
each `Int` and looks up a corresponding `String` from a `romanNumeralDict`
dictionary. This means the outer `for await in` loop iterates over `String`
instances instead of the underlying `Int` values that `Counter` produces.
Also, the dictionary doesn’t provide a key for `4`, and the closure throws an
error for any key it can’t look up, so receiving this value from `Counter`
ends the modified sequence with an error.

## See Also

### Transforming purchase intents

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncCompactMapSequence<PurchaseIntent.PurchaseIntents, ElementOfResult>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements, omitting results that don’t return a value.

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncThrowingCompactMapSequence<PurchaseIntent.PurchaseIntents,
ElementOfResult>`

Creates an asynchronous sequence that maps an error-throwing closure over the
base sequence’s elements, omitting results that don’t return a value.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncThrowingFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given error-throwing transformation with each element of this sequence.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given transformation with each element of this sequence.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements.

`func prefix(Int) -> AsyncPrefixSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, up to the specified maximum length,
containing the initial elements of the base asynchronous sequence.

`func prefix(while: (PurchaseIntent) -> Bool) ->
AsyncPrefixWhileSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, containing the initial, consecutive elements
of the base sequence that satisfy the given predicate.

`func reduce<Result>(Result, (Result, PurchaseIntent) -> Result) -> Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure.

`func reduce<Result>(into: Result, (inout Result, PurchaseIntent) -> Void) ->
Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure, given a mutable initial value.

Instance Method

# prefix(_:)

Returns an asynchronous sequence, up to the specified maximum length,
containing the initial elements of the base asynchronous sequence.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    func prefix(_ count: Int) -> AsyncPrefixSequence<PurchaseIntent.PurchaseIntents>

##  Parameters

`count`

    

The maximum number of elements to return. The value of `count` must be greater
than or equal to zero.

## Return Value

An asynchronous sequence starting at the beginning of the base sequence with
at most `count` elements.

## Discussion

Use `prefix(_:)` to reduce the number of elements produced by the asynchronous
sequence.

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `10`. The `prefix(_:)` method causes the modified sequence
to pass through the first six values, then end.

If the count passed to `prefix(_:)` exceeds the number of elements in the base
sequence, the result contains all of the elements in the sequence.

## See Also

### Transforming purchase intents

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncCompactMapSequence<PurchaseIntent.PurchaseIntents, ElementOfResult>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements, omitting results that don’t return a value.

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncThrowingCompactMapSequence<PurchaseIntent.PurchaseIntents,
ElementOfResult>`

Creates an asynchronous sequence that maps an error-throwing closure over the
base sequence’s elements, omitting results that don’t return a value.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncThrowingFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given error-throwing transformation with each element of this sequence.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given transformation with each element of this sequence.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncThrowingMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given error-throwing closure
over the asynchronous sequence’s elements.

`func prefix(while: (PurchaseIntent) -> Bool) ->
AsyncPrefixWhileSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, containing the initial, consecutive elements
of the base sequence that satisfy the given predicate.

`func reduce<Result>(Result, (Result, PurchaseIntent) -> Result) -> Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure.

`func reduce<Result>(into: Result, (inout Result, PurchaseIntent) -> Void) ->
Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure, given a mutable initial value.

Instance Method

# prefix(while:)

Returns an asynchronous sequence, containing the initial, consecutive elements
of the base sequence that satisfy the given predicate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    @preconcurrency
    func prefix(while predicate: @escaping @Sendable (PurchaseIntent) async -> Bool) rethrows -> AsyncPrefixWhileSequence<PurchaseIntent.PurchaseIntents>

##  Parameters

`predicate`

    

A closure that takes an element as a parameter and returns a Boolean value
indicating whether the element should be included in the modified sequence.

## Return Value

An asynchronous sequence of the initial, consecutive elements that satisfy
`predicate`.

## Discussion

Use `prefix(while:)` to produce values while elements from the base sequence
meet a condition you specify. The modified sequence ends when the predicate
closure returns `false`.

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `10`. The `prefix(while:)` method causes the modified
sequence to pass along values so long as they aren’t divisible by `2` and `3`.
Upon reaching `6`, the sequence ends:

## See Also

### Transforming purchase intents

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncCompactMapSequence<PurchaseIntent.PurchaseIntents, ElementOfResult>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements, omitting results that don’t return a value.

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncThrowingCompactMapSequence<PurchaseIntent.PurchaseIntents,
ElementOfResult>`

Creates an asynchronous sequence that maps an error-throwing closure over the
base sequence’s elements, omitting results that don’t return a value.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncThrowingFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given error-throwing transformation with each element of this sequence.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given transformation with each element of this sequence.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncThrowingMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given error-throwing closure
over the asynchronous sequence’s elements.

`func prefix(Int) -> AsyncPrefixSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, up to the specified maximum length,
containing the initial elements of the base asynchronous sequence.

`func reduce<Result>(Result, (Result, PurchaseIntent) -> Result) -> Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure.

`func reduce<Result>(into: Result, (inout Result, PurchaseIntent) -> Void) ->
Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure, given a mutable initial value.

Generic Instance Method

# reduce(_:_:)

Returns the result of combining the elements of the asynchronous sequence
using the given closure.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    func reduce<Result>(
        _ initialResult: Result,
        _ nextPartialResult: (Result, PurchaseIntent) async throws -> Result
    ) async rethrows -> Result

##  Parameters

`initialResult`

    

The value to use as the initial accumulating value. The `nextPartialResult`
closure receives `initialResult` the first time the closure runs.

`nextPartialResult`

    

A closure that combines an accumulating value and an element of the
asynchronous sequence into a new accumulating value, for use in the next call
of the `nextPartialResult` closure or returned to the caller.

## Return Value

The final accumulated value. If the sequence has no elements, the result is
`initialResult`.

## Discussion

Use the `reduce(_:_:)` method to produce a single value from the elements of
an entire sequence. For example, you can use this method on an sequence of
numbers to find their sum or product.

The `nextPartialResult` closure executes sequentially with an accumulating
value initialized to `initialResult` and each element of the sequence.

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `4`. The `reduce(_:_:)` method sums the values received
from the asynchronous sequence.

## See Also

### Transforming purchase intents

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncCompactMapSequence<PurchaseIntent.PurchaseIntents, ElementOfResult>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements, omitting results that don’t return a value.

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncThrowingCompactMapSequence<PurchaseIntent.PurchaseIntents,
ElementOfResult>`

Creates an asynchronous sequence that maps an error-throwing closure over the
base sequence’s elements, omitting results that don’t return a value.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncThrowingFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given error-throwing transformation with each element of this sequence.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given transformation with each element of this sequence.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncThrowingMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given error-throwing closure
over the asynchronous sequence’s elements.

`func prefix(Int) -> AsyncPrefixSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, up to the specified maximum length,
containing the initial elements of the base asynchronous sequence.

`func prefix(while: (PurchaseIntent) -> Bool) ->
AsyncPrefixWhileSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, containing the initial, consecutive elements
of the base sequence that satisfy the given predicate.

`func reduce<Result>(into: Result, (inout Result, PurchaseIntent) -> Void) ->
Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure, given a mutable initial value.

Generic Instance Method

# reduce(into:_:)

Returns the result of combining the elements of the asynchronous sequence
using the given closure, given a mutable initial value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    func reduce<Result>(
        into initialResult: Result,
        _ updateAccumulatingResult: (inout Result, PurchaseIntent) async throws -> Void
    ) async rethrows -> Result

##  Parameters

`initialResult`

    

The value to use as the initial accumulating value. The `nextPartialResult`
closure receives `initialResult` the first time the closure executes.

`nextPartialResult`

    

A closure that combines an accumulating value and an element of the
asynchronous sequence into a new accumulating value, for use in the next call
of the `nextPartialResult` closure or returned to the caller.

## Return Value

The final accumulated value. If the sequence has no elements, the result is
`initialResult`.

## Discussion

Use the `reduce(into:_:)` method to produce a single value from the elements
of an entire sequence. For example, you can use this method on a sequence of
numbers to find their sum or product.

The `nextPartialResult` closure executes sequentially with an accumulating
value initialized to `initialResult` and each element of the sequence.

Prefer this method over `reduce(_:_:)` for efficiency when the result is a
copy-on-write type, for example an `Array` or `Dictionary`.

## See Also

### Transforming purchase intents

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncCompactMapSequence<PurchaseIntent.PurchaseIntents, ElementOfResult>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements, omitting results that don’t return a value.

`func compactMap<ElementOfResult>((PurchaseIntent) -> ElementOfResult?) ->
AsyncThrowingCompactMapSequence<PurchaseIntent.PurchaseIntents,
ElementOfResult>`

Creates an asynchronous sequence that maps an error-throwing closure over the
base sequence’s elements, omitting results that don’t return a value.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncThrowingFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given error-throwing transformation with each element of this sequence.

`func flatMap<SegmentOfResult>((PurchaseIntent) -> SegmentOfResult) ->
AsyncFlatMapSequence<PurchaseIntent.PurchaseIntents, SegmentOfResult>`

Creates an asynchronous sequence that concatenates the results of calling the
given transformation with each element of this sequence.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given closure over the
asynchronous sequence’s elements.

`func map<Transformed>((PurchaseIntent) -> Transformed) ->
AsyncThrowingMapSequence<PurchaseIntent.PurchaseIntents, Transformed>`

Creates an asynchronous sequence that maps the given error-throwing closure
over the asynchronous sequence’s elements.

`func prefix(Int) -> AsyncPrefixSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, up to the specified maximum length,
containing the initial elements of the base asynchronous sequence.

`func prefix(while: (PurchaseIntent) -> Bool) ->
AsyncPrefixWhileSequence<PurchaseIntent.PurchaseIntents>`

Returns an asynchronous sequence, containing the initial, consecutive elements
of the base sequence that satisfy the given predicate.

`func reduce<Result>(Result, (Result, PurchaseIntent) -> Result) -> Result`

Returns the result of combining the elements of the asynchronous sequence
using the given closure.

Instance Method

# drop(while:)

Omits elements from the base asynchronous sequence until a given closure
returns false, after which it passes through all remaining elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    @preconcurrency
    func drop(while predicate: @escaping @Sendable (PurchaseIntent) async -> Bool) -> AsyncDropWhileSequence<PurchaseIntent.PurchaseIntents>

##  Parameters

`predicate`

    

A closure that takes an element as a parameter and returns a Boolean value
indicating whether to drop the element from the modified sequence.

## Return Value

An asynchronous sequence that skips over values from the base sequence until
the provided closure returns `false`.

## Discussion

Use `drop(while:)` to omit elements from an asynchronous sequence until the
element received meets a condition you specify.

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `10`. The `drop(while:)` method causes the modified
sequence to ignore received values until it encounters one that is divisible
by `3`:

After the predicate returns `false`, the sequence never executes it again, and
from then on the sequence passes through elements from its underlying sequence
as-is.

## See Also

### Excluding purchase intents

`func dropFirst(Int) ->
AsyncDropFirstSequence<PurchaseIntent.PurchaseIntents>`

Omits a specified number of elements from the base asynchronous sequence, then
passes through all remaining elements.

Instance Method

# dropFirst(_:)

Omits a specified number of elements from the base asynchronous sequence, then
passes through all remaining elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 16.4+  Xcode 11.0+

    
    
    func dropFirst(_ count: Int = 1) -> AsyncDropFirstSequence<PurchaseIntent.PurchaseIntents>

##  Parameters

`count`

    

The number of elements to drop from the beginning of the sequence. `count`
must be greater than or equal to zero.

## Return Value

An asynchronous sequence that drops the first `count` elements from the base
sequence.

## Discussion

Use `dropFirst(_:)` when you want to drop the first _n_ elements from the base
sequence and pass through the remaining elements.

In this example, an asynchronous sequence called `Counter` produces `Int`
values from `1` to `10`. The `dropFirst(_:)` method causes the modified
sequence to ignore the values `1` through `3`, and instead emit `4` through
`10`:

If the number of elements to drop exceeds the number of elements in the
sequence, the result is an empty sequence.

## See Also

### Excluding purchase intents

`func drop(while: (PurchaseIntent) -> Bool) ->
AsyncDropWhileSequence<PurchaseIntent.PurchaseIntents>`

Omits elements from the base asynchronous sequence until a given closure
returns false, after which it passes through all remaining elements.
