Instance Property

# result

The value the request returns after it executes.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var result: Any? { get }

## Discussion

Use `resultType` to determine the kind of value this property contains, and
then cast to the appropriate type as the following example shows:

## See Also

### Accessing the Result

`var resultType: NSBatchDeleteRequestResultType`

The data type of the request’s result value.

`enum NSBatchDeleteRequestResultType`

The types of result a batch delete request can provide when it executes.

Instance Property

# resultType

The data type of the request’s result value.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var resultType: NSBatchDeleteRequestResultType { get }

## Discussion

This property’s value is set to the request’s `resultType` property.

## See Also

### Accessing the Result

`var result: Any?`

The value the request returns after it executes.

`enum NSBatchDeleteRequestResultType`

The types of result a batch delete request can provide when it executes.

