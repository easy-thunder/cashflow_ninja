Rails.application.routes.draw do
  get 'bank_accounts/select'
  get 'bank_accounts/index'
  get 'bank_accounts/create'
  get 'bank_accounts/destroy'
  get 'bank_accounts/update'
  resources :bank_accounts, only: [:create, :destroy, :update, :index, :select]
  resources :users, only: [:create, :destroy, :update]
  post 'users/signin' # this probably needs to be a sessions
  resources :families, only: [:create, :destroy]

  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
