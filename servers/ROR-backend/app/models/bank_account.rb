class BankAccount < ApplicationRecord
  has_many :user_bank_accounts
  has_many :users, through: :user_bank_accounts
  has_many :family_bank_accounts
  has_many :families, through: :family_bank_accounts

  has_many :transactions

  enum account_type: { family: 0, personal: 1 }

  def account_type_name
    account_type == "family" ? "Family Bank Account" : "Personal Bank Account"
  end
end