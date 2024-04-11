Instance Property

# result

The result of a batch-insertion request.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var result: Any? { get }

## Discussion

Cast the result to the type corresponding to `resultType` to inspect it. The
following example shows how to inspect a result type of
`NSBatchInsertRequestResultType.statusOnly`.

## See Also

### Accessing Results

`var resultType: NSBatchInsertRequestResultType`

The type of result that Core Data returns from this request.

`enum NSBatchInsertRequestResultType`

Result types for a batch-insertion request.

Instance Property

# resultType

The type of result that Core Data returns from this request.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var resultType: NSBatchInsertRequestResultType { get }

## See Also

### Accessing Results

`var result: Any?`

The result of a batch-insertion request.

`enum NSBatchInsertRequestResultType`

Result types for a batch-insertion request.

