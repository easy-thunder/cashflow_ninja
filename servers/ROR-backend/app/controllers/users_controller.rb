class UsersController < ApplicationController
  # POST /users
  def create
    @user = User.new(user_params)
    if @user.save
      render json: @user, status: :created
    else
      render json: { errors: @user.errors.full_messages }, status: :unprocessable_entity
    end
  end

  # POST /users/signin
  # POST /users/signin
  def signin
    @user = User.find_by(email: params[:email])
    if @user && @user.authenticate(params[:password])
      # User authenticated, create session
      session[:user_id] = @user.id
      render json: { message: "User signed in successfully", user_id: @user.id }, status: :ok
    else
      render json: { error: "Invalid email or password" }, status: :unauthorized
    end
  end

  # DELETE /users/:id
  def delete
    @user = User.find(params[:id])
    @user.destroy
    head :no_content
  end

  # PATCH/PUT /users/:id
  def update
    @user = User.find(params[:id])
    if @user.update(user_params)
      render json: @user
    else
      render json: { errors: @user.errors.full_messages }, status: :unprocessable_entity
    end
  end

  private

  def user_params
    params.require(:user).permit(:email, :password, :is_admin, :can_view_all_accounts, :mfa_enabled)
  end
end