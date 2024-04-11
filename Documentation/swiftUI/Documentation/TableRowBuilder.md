Type Method

# buildBlock(_:)

Creates a single row result.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C>(_ content: C) -> C where Value == C.TableRowValue, C : TableRowContent

## See Also

### Building a row from sources

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableRowContent<Value, (C0,
C1)>`

Creates a row result from two sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> TupleTableRowContent<Value,
(C0, C1, C2)>`

Creates a row result from three sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableRowContent<Value, (C0, C1, C2, C3)>`

Creates a row result from four sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4)>`

Creates a row result from five sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5)>`

Creates a row result from six sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a row result from seven sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7)>`

Creates a row result from eight sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5,
C6, C7, C8)>`

Creates a row result from nine sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableRowContent<Value, (C0, C1, C2, C3,
C4, C5, C6, C7, C8, C9)>`

Creates a row result from ten sources.

Available when `Value` conforms to `Identifiable`.

Type Method

# buildBlock(_:_:)

Creates a row result from two sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1>(
        _ c0: C0,
        _ c1: C1
    ) -> TupleTableRowContent<Value, (C0, C1)> where Value == C0.TableRowValue, C0 : TableRowContent, C1 : TableRowContent, C0.TableRowValue == C1.TableRowValue

Available when `Value` conforms to `Identifiable`.

## See Also

### Building a row from sources

`static func buildBlock<C>(C) -> C`

Creates a single row result.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> TupleTableRowContent<Value,
(C0, C1, C2)>`

Creates a row result from three sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableRowContent<Value, (C0, C1, C2, C3)>`

Creates a row result from four sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4)>`

Creates a row result from five sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5)>`

Creates a row result from six sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a row result from seven sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7)>`

Creates a row result from eight sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5,
C6, C7, C8)>`

Creates a row result from nine sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableRowContent<Value, (C0, C1, C2, C3,
C4, C5, C6, C7, C8, C9)>`

Creates a row result from ten sources.

Available when `Value` conforms to `Identifiable`.

Type Method

# buildBlock(_:_:_:)

Creates a row result from three sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2
    ) -> TupleTableRowContent<Value, (C0, C1, C2)> where Value == C0.TableRowValue, C0 : TableRowContent, C1 : TableRowContent, C2 : TableRowContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue

Available when `Value` conforms to `Identifiable`.

## See Also

### Building a row from sources

`static func buildBlock<C>(C) -> C`

Creates a single row result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableRowContent<Value, (C0,
C1)>`

Creates a row result from two sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableRowContent<Value, (C0, C1, C2, C3)>`

Creates a row result from four sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4)>`

Creates a row result from five sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5)>`

Creates a row result from six sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a row result from seven sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7)>`

Creates a row result from eight sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5,
C6, C7, C8)>`

Creates a row result from nine sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableRowContent<Value, (C0, C1, C2, C3,
C4, C5, C6, C7, C8, C9)>`

Creates a row result from ten sources.

Available when `Value` conforms to `Identifiable`.

Type Method

# buildBlock(_:_:_:_:)

Creates a row result from four sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3
    ) -> TupleTableRowContent<Value, (C0, C1, C2, C3)> where Value == C0.TableRowValue, C0 : TableRowContent, C1 : TableRowContent, C2 : TableRowContent, C3 : TableRowContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue

Available when `Value` conforms to `Identifiable`.

## See Also

### Building a row from sources

`static func buildBlock<C>(C) -> C`

Creates a single row result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableRowContent<Value, (C0,
C1)>`

Creates a row result from two sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> TupleTableRowContent<Value,
(C0, C1, C2)>`

Creates a row result from three sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4)>`

Creates a row result from five sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5)>`

Creates a row result from six sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a row result from seven sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7)>`

Creates a row result from eight sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5,
C6, C7, C8)>`

Creates a row result from nine sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableRowContent<Value, (C0, C1, C2, C3,
C4, C5, C6, C7, C8, C9)>`

Creates a row result from ten sources.

Available when `Value` conforms to `Identifiable`.

Type Method

# buildBlock(_:_:_:_:_:)

Creates a row result from five sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4
    ) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4)> where Value == C0.TableRowValue, C0 : TableRowContent, C1 : TableRowContent, C2 : TableRowContent, C3 : TableRowContent, C4 : TableRowContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue

Available when `Value` conforms to `Identifiable`.

## See Also

### Building a row from sources

`static func buildBlock<C>(C) -> C`

Creates a single row result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableRowContent<Value, (C0,
C1)>`

Creates a row result from two sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> TupleTableRowContent<Value,
(C0, C1, C2)>`

Creates a row result from three sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableRowContent<Value, (C0, C1, C2, C3)>`

Creates a row result from four sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5)>`

Creates a row result from six sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a row result from seven sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7)>`

Creates a row result from eight sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5,
C6, C7, C8)>`

Creates a row result from nine sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableRowContent<Value, (C0, C1, C2, C3,
C4, C5, C6, C7, C8, C9)>`

Creates a row result from ten sources.

Available when `Value` conforms to `Identifiable`.

Type Method

# buildBlock(_:_:_:_:_:_:)

Creates a row result from six sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5
    ) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5)> where Value == C0.TableRowValue, C0 : TableRowContent, C1 : TableRowContent, C2 : TableRowContent, C3 : TableRowContent, C4 : TableRowContent, C5 : TableRowContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue, C4.TableRowValue == C5.TableRowValue

Available when `Value` conforms to `Identifiable`.

## See Also

### Building a row from sources

`static func buildBlock<C>(C) -> C`

Creates a single row result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableRowContent<Value, (C0,
C1)>`

Creates a row result from two sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> TupleTableRowContent<Value,
(C0, C1, C2)>`

Creates a row result from three sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableRowContent<Value, (C0, C1, C2, C3)>`

Creates a row result from four sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4)>`

Creates a row result from five sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a row result from seven sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7)>`

Creates a row result from eight sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5,
C6, C7, C8)>`

Creates a row result from nine sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableRowContent<Value, (C0, C1, C2, C3,
C4, C5, C6, C7, C8, C9)>`

Creates a row result from ten sources.

Available when `Value` conforms to `Identifiable`.

Type Method

# buildBlock(_:_:_:_:_:_:_:)

Creates a row result from seven sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6
    ) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6)> where Value == C0.TableRowValue, C0 : TableRowContent, C1 : TableRowContent, C2 : TableRowContent, C3 : TableRowContent, C4 : TableRowContent, C5 : TableRowContent, C6 : TableRowContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue, C4.TableRowValue == C5.TableRowValue, C5.TableRowValue == C6.TableRowValue

Available when `Value` conforms to `Identifiable`.

## See Also

### Building a row from sources

`static func buildBlock<C>(C) -> C`

Creates a single row result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableRowContent<Value, (C0,
C1)>`

Creates a row result from two sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> TupleTableRowContent<Value,
(C0, C1, C2)>`

Creates a row result from three sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableRowContent<Value, (C0, C1, C2, C3)>`

Creates a row result from four sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4)>`

Creates a row result from five sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5)>`

Creates a row result from six sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7)>`

Creates a row result from eight sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5,
C6, C7, C8)>`

Creates a row result from nine sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableRowContent<Value, (C0, C1, C2, C3,
C4, C5, C6, C7, C8, C9)>`

Creates a row result from ten sources.

Available when `Value` conforms to `Identifiable`.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:)

Creates a row result from eight sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7
    ) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7)> where Value == C0.TableRowValue, C0 : TableRowContent, C1 : TableRowContent, C2 : TableRowContent, C3 : TableRowContent, C4 : TableRowContent, C5 : TableRowContent, C6 : TableRowContent, C7 : TableRowContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue, C4.TableRowValue == C5.TableRowValue, C5.TableRowValue == C6.TableRowValue, C6.TableRowValue == C7.TableRowValue

Available when `Value` conforms to `Identifiable`.

## See Also

### Building a row from sources

`static func buildBlock<C>(C) -> C`

Creates a single row result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableRowContent<Value, (C0,
C1)>`

Creates a row result from two sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> TupleTableRowContent<Value,
(C0, C1, C2)>`

Creates a row result from three sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableRowContent<Value, (C0, C1, C2, C3)>`

Creates a row result from four sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4)>`

Creates a row result from five sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5)>`

Creates a row result from six sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a row result from seven sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5,
C6, C7, C8)>`

Creates a row result from nine sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableRowContent<Value, (C0, C1, C2, C3,
C4, C5, C6, C7, C8, C9)>`

Creates a row result from ten sources.

Available when `Value` conforms to `Identifiable`.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:)

Creates a row result from nine sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8
    ) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7, C8)> where Value == C0.TableRowValue, C0 : TableRowContent, C1 : TableRowContent, C2 : TableRowContent, C3 : TableRowContent, C4 : TableRowContent, C5 : TableRowContent, C6 : TableRowContent, C7 : TableRowContent, C8 : TableRowContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue, C4.TableRowValue == C5.TableRowValue, C5.TableRowValue == C6.TableRowValue, C6.TableRowValue == C7.TableRowValue, C7.TableRowValue == C8.TableRowValue

Available when `Value` conforms to `Identifiable`.

## See Also

### Building a row from sources

`static func buildBlock<C>(C) -> C`

Creates a single row result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableRowContent<Value, (C0,
C1)>`

Creates a row result from two sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> TupleTableRowContent<Value,
(C0, C1, C2)>`

Creates a row result from three sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableRowContent<Value, (C0, C1, C2, C3)>`

Creates a row result from four sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4)>`

Creates a row result from five sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5)>`

Creates a row result from six sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a row result from seven sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7)>`

Creates a row result from eight sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> TupleTableRowContent<Value, (C0, C1, C2, C3,
C4, C5, C6, C7, C8, C9)>`

Creates a row result from ten sources.

Available when `Value` conforms to `Identifiable`.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:_:)

Creates a row result from ten sources.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8,
        _ c9: C9
    ) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7, C8, C9)> where Value == C0.TableRowValue, C0 : TableRowContent, C1 : TableRowContent, C2 : TableRowContent, C3 : TableRowContent, C4 : TableRowContent, C5 : TableRowContent, C6 : TableRowContent, C7 : TableRowContent, C8 : TableRowContent, C9 : TableRowContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue, C4.TableRowValue == C5.TableRowValue, C5.TableRowValue == C6.TableRowValue, C6.TableRowValue == C7.TableRowValue, C7.TableRowValue == C8.TableRowValue, C8.TableRowValue == C9.TableRowValue

Available when `Value` conforms to `Identifiable`.

## See Also

### Building a row from sources

`static func buildBlock<C>(C) -> C`

Creates a single row result.

`static func buildBlock<C0, C1>(C0, C1) -> TupleTableRowContent<Value, (C0,
C1)>`

Creates a row result from two sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> TupleTableRowContent<Value,
(C0, C1, C2)>`

Creates a row result from three sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) ->
TupleTableRowContent<Value, (C0, C1, C2, C3)>`

Creates a row result from four sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4)>`

Creates a row result from five sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5)>`

Creates a row result from six sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6)>`

Creates a row result from seven sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7)>`

Creates a row result from eight sources.

Available when `Value` conforms to `Identifiable`.

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5,
C6, C7, C8)>`

Creates a row result from nine sources.

Available when `Value` conforms to `Identifiable`.

Type Method

# buildIf(_:)

Creates a row result for conditional statements.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildIf<C>(_ content: C?) -> C? where Value == C.TableRowValue, C : TableRowContent

Available when `Value` conforms to `Identifiable`.

## Discussion

This method provides support for “if” statements in multi-statement closures,
producing an optional value that is visible only when the condition evaluates
to `true`.

## See Also

### Building a row from conditionals

`static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>`

Creates a row result for the first of two row content alternatives.

Available when `Value` conforms to `Identifiable`.

`static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>`

Creates a row result for the second of two row content alternatives.

Available when `Value` conforms to `Identifiable`.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildEither(first:)

Creates a row result for the first of two row content alternatives.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F> where Value == T.TableRowValue, T : TableRowContent, F : TableRowContent, T.TableRowValue == F.TableRowValue

Available when `Value` conforms to `Identifiable`.

## Discussion

This method provides support for “if” statements in multi-statement closures,
producing conditional content for the “then” branch.

## See Also

### Building a row from conditionals

`static func buildIf<C>(C?) -> C?`

Creates a row result for conditional statements.

Available when `Value` conforms to `Identifiable`.

`static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>`

Creates a row result for the second of two row content alternatives.

Available when `Value` conforms to `Identifiable`.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildEither(second:)

Creates a row result for the second of two row content alternatives.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where Value == T.TableRowValue, T : TableRowContent, F : TableRowContent, T.TableRowValue == F.TableRowValue

Available when `Value` conforms to `Identifiable`.

## Discussion

This method provides support for “if” statements in multi-statement closures,
producing conditional content for the “else” branch.

## See Also

### Building a row from conditionals

`static func buildIf<C>(C?) -> C?`

Creates a row result for conditional statements.

Available when `Value` conforms to `Identifiable`.

`static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>`

Creates a row result for the first of two row content alternatives.

Available when `Value` conforms to `Identifiable`.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildExpression(_:)

Builds an expression within the builder.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildExpression<Content>(_ content: Content) -> Content where Value == Content.TableRowValue, Content : TableRowContent

## See Also

### Building a row from conditionals

`static func buildIf<C>(C?) -> C?`

Creates a row result for conditional statements.

Available when `Value` conforms to `Identifiable`.

`static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>`

Creates a row result for the first of two row content alternatives.

Available when `Value` conforms to `Identifiable`.

`static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>`

Creates a row result for the second of two row content alternatives.

Available when `Value` conforms to `Identifiable`.

