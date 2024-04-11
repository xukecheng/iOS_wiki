Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration `

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.

## See Also

### Custom button styles

`typealias Configuration`

The properties of a button.

`associatedtype Body : View`

A view that represents the body of a button.

**Required**

Type Alias

# ButtonStyle.Configuration

The properties of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    typealias Configuration = ButtonStyleConfiguration

## See Also

### Custom button styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a button.

**Required**

` associatedtype Body : View`

A view that represents the body of a button.

**Required**

Associated Type

# Body

A view that represents the body of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Custom button styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a button.

**Required**

` typealias Configuration`

The properties of a button.

