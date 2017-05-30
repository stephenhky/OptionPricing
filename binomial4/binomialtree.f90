module binomialtree
implicit none
private
public tree_stockprice, eurocall

contains

function tree_stockprice(S0, u, d, i, j) result(price)
  real, intent(in) :: S0, u, d
  integer, intent(in) :: i, j
  real :: price
  ! using Python array indexing (start from 0)
  price = S0 * u**(i-j) * d**j
end function tree_stockprice

function eurocall(S0, X, u, d, nbsteps) result(price)
  real, intent(in) :: S0, X, u, d
  integer, intent(in) :: nbsteps
  real :: price
  real, dimension(nbsteps+1) :: pricearr
  integer :: i, j
  do j = 0, nbsteps
     pricearr(j+1) = max(tree_stockprice(S0, u, d, nbsteps, j)-X, 0.0)
  end do
  do i = nbsteps-1, 0, 01
     do j = 0, i
        ! calculation of price
     end do
  end do
  price = pricearr(1)
end function
  
end module

! compiling
! > f2py -h binomialtree.pyf -m binomialtree binomialtree.f90
! > f2py -c binomialtree.pyf binomialtree.f90

