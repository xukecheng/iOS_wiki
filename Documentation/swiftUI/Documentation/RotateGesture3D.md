Initializer

# init(constrainedToAxis:minimumAngleDelta:)

Creates a rotation gesture with a minimum delta for the gesture to start and
axis to constrain measurement of rotation.

visionOS 1.0+

    
    
    init(
        constrainedToAxis: RotationAxis3D? = nil,
        minimumAngleDelta: Angle = .degrees(1)
    )

##  Parameters

`constrainedToAxis`

    

The 3D axis about which rotation is measured.

`minimumAngleDelta`

    

The minimum delta required before the gesture starts. The default value is a
one-degree angle.

## Discussion

If the constrained axis is `nil`, the gesture measures unconstrained 3D
rotation.

## See Also

### Creating the gesture

`var minimumAngleDelta: Angle`

The minimum angle delta before the gesture becomes active.

`var constrainedAxis: RotationAxis3D?`

An axis around which the rotation is constrained.

Instance Property

# minimumAngleDelta

The minimum angle delta before the gesture becomes active.

visionOS 1.0+

    
    
    var minimumAngleDelta: Angle

## See Also

### Creating the gesture

`init(constrainedToAxis: RotationAxis3D?, minimumAngleDelta: Angle)`

Creates a rotation gesture with a minimum delta for the gesture to start and
axis to constrain measurement of rotation.

`var constrainedAxis: RotationAxis3D?`

An axis around which the rotation is constrained.

Instance Property

# constrainedAxis

An axis around which the rotation is constrained.

visionOS 1.0+

    
    
    var constrainedAxis: RotationAxis3D?

## Discussion

If the axis is `nil`, the rotation is unconstrained.

## See Also

### Creating the gesture

`init(constrainedToAxis: RotationAxis3D?, minimumAngleDelta: Angle)`

Creates a rotation gesture with a minimum delta for the gesture to start and
axis to constrain measurement of rotation.

`var minimumAngleDelta: Angle`

The minimum angle delta before the gesture becomes active.

