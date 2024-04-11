Enumeration Case

# NSDeleteRule.noActionDeleteRule

A rule that prevents modification of the referenced managed objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case noActionDeleteRule = 0

## Discussion

If you use this delete rule, make sure you delete any referenced managed
objects or nullify their inverse relationships. Otherwise, those objects will
reference an object that doesn’t exist, and your persistent store will be in
an inconsistent state.

## See Also

### Delete Rules

`case nullifyDeleteRule`

A rule that nullifies the inverse relationship of the referenced managed
objects.

`case cascadeDeleteRule`

A rule that deletes the referenced managed objects.

`case denyDeleteRule`

A rule that prevents the deletion of the owning managed object if the
relationship has references to other objects.

Enumeration Case

# NSDeleteRule.nullifyDeleteRule

A rule that nullifies the inverse relationship of the referenced managed
objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case nullifyDeleteRule = 1

## See Also

### Delete Rules

`case noActionDeleteRule`

A rule that prevents modification of the referenced managed objects.

`case cascadeDeleteRule`

A rule that deletes the referenced managed objects.

`case denyDeleteRule`

A rule that prevents the deletion of the owning managed object if the
relationship has references to other objects.

Enumeration Case

# NSDeleteRule.cascadeDeleteRule

A rule that deletes the referenced managed objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case cascadeDeleteRule = 2

## See Also

### Delete Rules

`case noActionDeleteRule`

A rule that prevents modification of the referenced managed objects.

`case nullifyDeleteRule`

A rule that nullifies the inverse relationship of the referenced managed
objects.

`case denyDeleteRule`

A rule that prevents the deletion of the owning managed object if the
relationship has references to other objects.

Enumeration Case

# NSDeleteRule.denyDeleteRule

A rule that prevents the deletion of the owning managed object if the
relationship has references to other objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case denyDeleteRule = 3

## See Also

### Delete Rules

`case noActionDeleteRule`

A rule that prevents modification of the referenced managed objects.

`case nullifyDeleteRule`

A rule that nullifies the inverse relationship of the referenced managed
objects.

`case cascadeDeleteRule`

A rule that deletes the referenced managed objects.

Enumeration Case

# NSDeleteRule.noActionDeleteRule

A rule that prevents modification of the referenced managed objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case noActionDeleteRule = 0

## Discussion

If you use this delete rule, make sure you delete any referenced managed
objects or nullify their inverse relationships. Otherwise, those objects will
reference an object that doesn’t exist, and your persistent store will be in
an inconsistent state.

## See Also

### Delete Rules

`case nullifyDeleteRule`

A rule that nullifies the inverse relationship of the referenced managed
objects.

`case cascadeDeleteRule`

A rule that deletes the referenced managed objects.

`case denyDeleteRule`

A rule that prevents the deletion of the owning managed object if the
relationship has references to other objects.

Enumeration Case

# NSDeleteRule.nullifyDeleteRule

A rule that nullifies the inverse relationship of the referenced managed
objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case nullifyDeleteRule = 1

## See Also

### Delete Rules

`case noActionDeleteRule`

A rule that prevents modification of the referenced managed objects.

`case cascadeDeleteRule`

A rule that deletes the referenced managed objects.

`case denyDeleteRule`

A rule that prevents the deletion of the owning managed object if the
relationship has references to other objects.

Enumeration Case

# NSDeleteRule.cascadeDeleteRule

A rule that deletes the referenced managed objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case cascadeDeleteRule = 2

## See Also

### Delete Rules

`case noActionDeleteRule`

A rule that prevents modification of the referenced managed objects.

`case nullifyDeleteRule`

A rule that nullifies the inverse relationship of the referenced managed
objects.

`case denyDeleteRule`

A rule that prevents the deletion of the owning managed object if the
relationship has references to other objects.

Enumeration Case

# NSDeleteRule.denyDeleteRule

A rule that prevents the deletion of the owning managed object if the
relationship has references to other objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case denyDeleteRule = 3

## See Also

### Delete Rules

`case noActionDeleteRule`

A rule that prevents modification of the referenced managed objects.

`case nullifyDeleteRule`

A rule that nullifies the inverse relationship of the referenced managed
objects.

`case cascadeDeleteRule`

A rule that deletes the referenced managed objects.

