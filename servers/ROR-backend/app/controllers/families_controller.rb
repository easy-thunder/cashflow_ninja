class FamiliesController < ApplicationController
  def create
    @family = Family.new(family_params)
    if @family.save
      # Create the associated user using the provided email and password
      @user = @family.users.build(email: params[:family][:email], password: params[:family][:password], is_admin: true, can_view_all_accounts: true)

      if @user.save
        render json: @family, status: :created
      else
        render json: { errors: @user.errors.full_messages }, status: :unprocessable_entity
      end
    else
      render json: { errors: @family.errors.full_messages }, status: :unprocessable_entity
    end
  end

  private

  def family_params
    params.require(:family).permit(:family_name, :email, :password)
  end
end
