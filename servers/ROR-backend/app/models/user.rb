class User < ApplicationRecord
  belongs_to :family
  has_many :goals
  has_many :bank_accounts
  has_one :financial_profile
  has_many :stocks_accounts
  has_many :account_integrations

  has_secure_password

  validates :email, presence: true, uniqueness: true, format: { with: /\A[\w+\-.]+@[a-z\d\-.]+\.[a-z]+\z/i, message: "must be a valid email address" }
  validates :password_digest, presence: true, length: { minimum: 7 }
  validate :password_complexity

  def password_complexity
    return unless :password_digest.present? && !:password_hash.match(/^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{7,}$/)
    errors.add :password, "must include at least one uppercase letter, one lowercase letter, one digit, and one symbol"
  end
end