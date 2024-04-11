Initializer

# init(configuration:)

Creates a new transition.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(configuration: BlurReplaceTransition.Configuration)

##  Parameters

`configuration`

    

the transition configuration.

## See Also

### Creating the transition

`var configuration: BlurReplaceTransition.Configuration`

The transition configuration.

`struct Configuration`

Configuration properties for a transition.

Instance Property

# configuration

The transition configuration.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var configuration: BlurReplaceTransition.Configuration

## See Also

### Creating the transition

`init(configuration: BlurReplaceTransition.Configuration)`

Creates a new transition.

`struct Configuration`

Configuration properties for a transition.

Structure

# BlurReplaceTransition.Configuration

Configuration properties for a transition.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct Configuration

## Topics

### Getting the transition configuration

`static let downUp: BlurReplaceTransition.Configuration`

A configuration that requests a transition that scales the view down while
removing it and up while inserting it.

`static let upUp: BlurReplaceTransition.Configuration`

A configuration that requests a transition that scales the view up while both
removing and inserting it.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Creating the transition

`init(configuration: BlurReplaceTransition.Configuration)`

Creates a new transition.

`var configuration: BlurReplaceTransition.Configuration`

The transition configuration.

