Instance Method

# resolve(in:)

Resolve to a concrete modifier in the given `environment`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func resolve(in environment: EnvironmentValues) -> Self.ResolvedModifier

**Required**

## See Also

### Resolving a modifier

`associatedtype ResolvedModifier : ViewModifier`

The type of modifier to use after being resolved.

**Required**

Associated Type

# ResolvedModifier

The type of modifier to use after being resolved.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype ResolvedModifier : ViewModifier

**Required**

## See Also

### Resolving a modifier

`func resolve(in: EnvironmentValues) -> Self.ResolvedModifier`

Resolve to a concrete modifier in the given `environment`.

**Required**

