Instance Property

# body

The contents of the command hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @CommandsBuilder
    var body: Self.Body { get }

**Required**

## Discussion

For any commands that you create, provide a computed `body` property that
defines the scene as a composition of other scenes. You can assemble a command
hierarchy from built-in commands that SwiftUI provides, as well as other
commands that you’ve defined.

## See Also

### Implementing commands

`associatedtype Body : Commands`

The type of commands that represents the body of this command hierarchy.

**Required**

Associated Type

# Body

The type of commands that represents the body of this command hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    associatedtype Body : Commands

**Required**

## Discussion

When you create custom commands, Swift infers this type from your
implementation of the required `body` property.

## See Also

### Implementing commands

`var body: Self.Body`

The contents of the command hierarchy.

**Required**

