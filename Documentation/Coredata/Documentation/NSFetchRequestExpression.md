Type Method

# expression(forFetch:context:countOnly:)

Returns an expression which will evaluate to the result of executing a fetch
request on a context.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func expression(
        forFetch fetch: NSExpression,
        context: NSExpression,
        countOnly countFlag: Bool
    ) -> NSExpression

##  Parameters

`fetch`

    

An expression that evaluates to an instance of `NSFetchRequest`.

`context`

    

An expression that evaluates to an instance of `NSManagedObjectContext`.

`countFlag`

    

If `true`, when the new expression is evaluated the managed object context
(from `context`) will perform `count(for:)` with the fetch request (from
`fetch`). If `false`, when the new expression is evaluated the managed object
context will perform `fetch(_:)` with the fetch request.

## Return Value

An expression which will evaluate to the result of executing a fetch request
(from `fetch`) on a managed object context (from `context`).

## See Also

### Related Documentation

Predicate Programming Guide

Core Data Programming Guide

Instance Property

# requestExpression

The expression for the receiver’s fetch request.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var requestExpression: NSExpression { get }

## Discussion

The expression must evaluate to an `NSFetchRequest` object.

## See Also

### Examining a Fetch Request Expression

`var contextExpression: NSExpression`

The expression for the receiver’s managed object context.

`var isCountOnlyRequest: Bool`

Returns a Boolean value that indicates whether the receiver represents a
count-only fetch request.

Instance Property

# contextExpression

The expression for the receiver’s managed object context.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var contextExpression: NSExpression { get }

## Discussion

The expression must evaluate to an `NSManagedObjectContext` object.

## See Also

### Examining a Fetch Request Expression

`var requestExpression: NSExpression`

The expression for the receiver’s fetch request.

`var isCountOnlyRequest: Bool`

Returns a Boolean value that indicates whether the receiver represents a
count-only fetch request.

Instance Property

# isCountOnlyRequest

Returns a Boolean value that indicates whether the receiver represents a
count-only fetch request.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isCountOnlyRequest: Bool { get }

## Discussion

`true` if the receiver represents a count-only fetch request, otherwise
`false`. If this method returns `false`, the managed object context (from the
`contextExpression`) will perform `fetch(_:)`: with the `requestExpression`;
if this method returns `true`, the managed object context will perform
`count(for:)` with the `requestExpression`.

## See Also

### Examining a Fetch Request Expression

`var requestExpression: NSExpression`

The expression for the receiver’s fetch request.

`var contextExpression: NSExpression`

The expression for the receiver’s managed object context.

Global Variable

# NSFetchRequestExpressionType

This constant specifies the fetch request expression type.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSFetchRequestExpressionType: NSExpression.ExpressionType

